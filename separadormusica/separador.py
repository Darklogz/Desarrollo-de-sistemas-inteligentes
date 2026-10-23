"""
separar_local.py

Usage:
    python separar_local.py                  # every song in ./canciones
    python separar_local.py mi_cancion.mp3   # a single file
"""
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import soundfile as sf
from tqdm import tqdm

# --- Config ---
MODEL = "htdemucs_6s"
STEMS = ["vocals", "drums", "bass", "guitar", "piano", "other"]
LABELS = {
    "vocals": "Voz",
    "drums": "Percusión",
    "bass": "Bajo",
    "guitar": "Guitarra",
    "piano": "Piano",
    "other": "Otros",
}
THRESHOLD_DB = -40.0   # below this = silence
WINDOW_SEC = 1.0
SOFT = 3.0             # dB scale of the decision margin
BLEED_DB = 25.0        # active window this far below the loudest stem = likely bleed
W_RECON = 0.2          # weight of the reconstruction score in the global confidence

SONGS_DIR = Path("canciones")
OUT_DIR = Path("separated")
RESULTS_DIR = Path("resultados")
EXTS = {".mp3", ".wav", ".flac", ".m4a", ".ogg"}


def rms_db(x):
    return 20 * np.log10(np.sqrt(np.mean(np.square(x)) + 1e-12) + 1e-12)


def to_stereo(a):
    return np.stack([a, a], axis=1) if a.ndim == 1 else a


def separate(song: Path) -> Path:
    stem_dir = OUT_DIR / MODEL / song.stem
    if all((stem_dir / f"{s}.wav").exists() for s in STEMS):
        print(f"  Stems ya existen, se omite la separación.")
        return stem_dir
    # Demucs prints its own progress bar in the terminal
    subprocess.run(
        [sys.executable, "-m", "demucs", "-n", MODEL, "-o", str(OUT_DIR), str(song)],
        check=True,
    )
    return stem_dir


def analyze(song: Path, stem_dir: Path):
    # Load stems
    stems_audio = {}
    sr = None
    for stem in STEMS:
        a, sr = sf.read(stem_dir / f"{stem}.wav")
        stems_audio[stem] = to_stereo(a)

    # Load original mix at the same sample rate
    ref_path = RESULTS_DIR / f"_{song.stem}_ref.wav"
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(song),
         "-ar", str(sr), "-ac", "2", str(ref_path)],
        check=True,
    )
    mix, _ = sf.read(ref_path)
    ref_path.unlink(missing_ok=True)
    mix = to_stereo(mix)

    n = min(len(mix), *(len(a) for a in stems_audio.values()))
    mix = mix[:n]

    # Reconstruction check (do the stems add back up to the original?)
    recon = sum(a[:n] for a in stems_audio.values())
    err = mix - recon
    sdr = 10 * np.log10((np.sum(mix ** 2) + 1e-12) / (np.sum(err ** 2) + 1e-12))
    recon_score = float(np.clip(sdr / 30.0, 0, 1)) * 100

    # Per-window dB for every stem
    win = int(sr * WINDOW_SEC)
    n_win = n // win
    dbs = np.zeros((len(STEMS), n_win))
    for i, stem in enumerate(STEMS):
        mono = stems_audio[stem][:n].mean(axis=1)
        for w in range(n_win):
            dbs[i, w] = rms_db(mono[w * win:(w + 1) * win])
    loudest = dbs.max(axis=0)

    # Confidence per stem
    rows = []
    for i, stem in enumerate(STEMS):
        db = dbs[i]
        active = db > THRESHOLD_DB

        p = 1 / (1 + np.exp(-(db - THRESHOLD_DB) / SOFT))
        margin_conf = float(np.mean(np.maximum(p, 1 - p)))

        bleed = active & ((db - loudest) < -BLEED_DB)
        purity = 1 - bleed.sum() / max(active.sum(), 1)

        rows.append({
            "Instrumento": LABELS[stem],
            "Presencia %": round(100 * active.mean(), 1),
            "Ventanas ambiguas %": round(100 * np.mean(np.abs(db - THRESHOLD_DB) < SOFT), 1),
            "Posible fuga %": round(100 * (1 - purity), 1),
            "Seguridad %": round(margin_conf * purity * 100, 1),
        })

    df = pd.DataFrame(rows)
    global_conf = (1 - W_RECON) * df["Seguridad %"].mean() + W_RECON * recon_score
    return df, float(sdr), float(global_conf)


def update_summary(song_name, df, sdr, global_conf):
    row = {"Canción": song_name, "SDR (dB)": round(sdr, 1),
           "Seguridad global %": round(global_conf, 1)}
    for _, r in df.iterrows():
        row[f"{r['Instrumento']} presencia %"] = r["Presencia %"]
        row[f"{r['Instrumento']} seguridad %"] = r["Seguridad %"]

    summary_path = RESULTS_DIR / "resumen.csv"
    if summary_path.exists():
        summary = pd.read_csv(summary_path)
        summary = summary[summary["Canción"] != song_name]
        summary = pd.concat([summary, pd.DataFrame([row])], ignore_index=True)
    else:
        summary = pd.DataFrame([row])
    summary.to_csv(summary_path, index=False)


def main():
    RESULTS_DIR.mkdir(exist_ok=True)

    if len(sys.argv) > 1:
        songs = [Path(a) for a in sys.argv[1:]]
    else:
        if not SONGS_DIR.exists():
            SONGS_DIR.mkdir()
            print(f"Carpeta '{SONGS_DIR}' creada. Pon tus canciones ahí y vuelve a correr.")
            return
        songs = sorted(p for p in SONGS_DIR.iterdir() if p.suffix.lower() in EXTS)

    if not songs:
        print("No se encontraron canciones.")
        return

    failed = []
    for song in tqdm(songs, desc="Canciones", unit="canción"):
        print(f"\n>>> {song.name}")
        try:
            stem_dir = separate(song)
            df, sdr, global_conf = analyze(song, stem_dir)
            df.to_csv(RESULTS_DIR / f"{song.stem}_confianza.csv", index=False)
            update_summary(song.stem, df, sdr, global_conf)
            print(df.to_string(index=False))
            print(f"SDR: {sdr:.1f} dB | SEGURIDAD GLOBAL: {global_conf:.1f}%")
        except Exception as e:
            failed.append(song.name)
            print(f"  ERROR con {song.name}: {e}")

    print(f"\nListo. Resumen en {RESULTS_DIR / 'resumen.csv'}")
    if failed:
        print(f"Fallaron: {', '.join(failed)}")


if __name__ == "__main__":
    main()