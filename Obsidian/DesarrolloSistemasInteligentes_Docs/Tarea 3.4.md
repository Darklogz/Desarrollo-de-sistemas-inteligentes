# Práctica: entrenar y probar un clasificador con Teachable Machine


**Herramienta:** colab.google.com
**Modalidad:** por equipos
**Entrega:** un solo archivo (PDF o Markdown en su repositorio) con las evidencias y respuestas que se piden abajo.

---

## 1. Objetivo

Entrenar un clasificador, medir qué tan bien funciona con pocos ejemplos, medir de nuevo con más ejemplos y, después, cambiar las opciones avanzadas para observar cómo se comporta el entrenamiento.

---

## 2. Antes de empezar: elijan el proyecto

Elijan **una** idea en la que la clase se vea en la imagen (no un estado interno como cansancio o miedo):

Programa para separar diferentes instrumentos de una canción


Mínimo **2 clases**. Escriban en su entrega el proyecto elegido y las clases.

---

## 3. Instrucciones

Hice un proyecto en google collab con python utilizando demucs de meta para separar los canales de audio de canciones para generar un resultado con los dierentes instrumentos separados

Codigo fuente:
# Instalador de dependencias

!pip install -q demucs soundfile numpy torchcodec
import os

import re

import subprocess

import sys

from pathlib import Path

  

import numpy as np

import soundfile as sf

from google.colab import files

from IPython.display import Audio, display

from tqdm.auto import tqdm

  

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

THRESHOLD_DB = -40.0  # below this = silence

WINDOW_SEC = 1.0

  

overall = tqdm(total=4, desc="Progreso general", position=0, bar_format="{desc}: {n}/{total} etapas |{bar}| {elapsed}")

  

# Stage 1: upload song

uploaded = files.upload()

song = Path(next(iter(uploaded)))

overall.update(1)

  

# Stage 2: separate with Demucs (live progress)

out_dir = Path("separated")

proc = subprocess.Popen(

    [sys.executable, "-u", "-m", "demucs", "-n", MODEL, "-o", str(out_dir), str(song)],

    stdout=subprocess.PIPE,

    stderr=subprocess.STDOUT,

    bufsize=0,

)

  

sep_bar = tqdm(total=100, desc="Separando (Demucs)", unit="%", position=1)

tail = ""

last_pct = 0

while True:

    chunk = proc.stdout.read(64)

    if not chunk:

        break

    tail = (tail + chunk.decode(errors="ignore"))[-3000:]

    matches = re.findall(r"(\d{1,3})%\|", tail[-200:])

    if matches:

        pct = min(int(matches[-1]), 100)

        if pct > last_pct:

            sep_bar.update(pct - last_pct)

            last_pct = pct

  

proc.wait()

if proc.returncode != 0:

    sep_bar.close()

    raise RuntimeError(f"Demucs failed (code {proc.returncode}). Last output:\n{tail}")

sep_bar.update(100 - last_pct)

sep_bar.close()

overall.update(1)

  

stem_dir = out_dir / MODEL / song.stem

  
  

# Stage 3: analyze activity per stem

def rms_db(x):

    return 20 * np.log10(np.sqrt(np.mean(np.square(x)) + 1e-12) + 1e-12)

  
  

result = {}

for stem in tqdm(STEMS, desc="Analizando stems", position=1):

    audio, sr = sf.read(stem_dir / f"{stem}.wav")

    if audio.ndim > 1:

        audio = audio.mean(axis=1)

    win = int(sr * WINDOW_SEC)

    n_windows = len(audio) // win

    active = [

        rms_db(audio[i * win:(i + 1) * win]) > THRESHOLD_DB

        for i in tqdm(range(n_windows), desc=f"  {LABELS[stem]}", leave=False, position=2)

    ]

    result[stem] = {"active": active, "pct": 100 * sum(active) / max(len(active), 1)}

overall.update(1)

  

# Stage 4: report + players

print("\n=== Presencia de instrumentos ===")

for stem, d in result.items():

    print(f"{LABELS[stem]:<10} {d['pct']:5.1f}% del tiempo")

  

print("\n=== Línea de tiempo (1 char = 1 s, █ = suena) ===")

for stem, d in result.items():

    print(f"{LABELS[stem]:<10} {''.join('█' if a else '·' for a in d['active'])}")

  

for stem in STEMS:

    print(f"\n{LABELS[stem]}")

    display(Audio(str(stem_dir / f"{stem}.wav")))

  

overall.update(1)

overall.close()

---

## 4. Evidencias que deben entregar
### Tabla de resultados (una por fase)

| Instrumento de la canción | Clase que predijo el modelo                               | Confianza (%) | ¿Acertó? |
| ------------------------- | --------------------------------------------------------- | ------------- | -------- |
| Voz                       | Es la que mejor detecta solo suele haber sonidos borrosos |               | Si       |
| Percusión                 | Detecta bien las percusiones                              |               | Si       |
| Bajo                      | Sorprendentemente es lo que mejor escucha                 |               | Si       |
| Guitarra                  | Toma la guitarra muy bien                                 |               | Si       |
| Piano                     | Suele no detectarla cuando suena                          |               | A veces  |
| Otro                      | Sonidos extraños u otros instrumentos                     |               | A veces  |



---

## 5. Experimentos con las opciones avanzadas

En **Advanced** encontrarán, según la versión de la página, ajustes como **Epochs**, **Batch Size** y **Learning Rate**. Usen los valores que ofrezca la lista; los de abajo son solo una guía de qué probar (un valor menor y uno mayor que el predeterminado).

| #   | Ajuste                                                              | Qué probar                                                               | Qué observar                                                                        |
| --- | ------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| 1   | **Epochs** (cuántas veces recorre los ejemplos)                     | Un valor muy bajo (por ejemplo, 1 a 5), el predeterminado y uno más alto | ¿Con pocas épocas falla en todo? ¿Con muchas deja de mejorar o empieza a memorizar? |
| 2   | **Learning Rate** (qué tan grande es cada ajuste)                   | Un valor mucho menor y otro mucho mayor que el predeterminado            | ¿Cuál se estabiliza? ¿Cuál se comporta de forma errática o no aprende?              |
| 3   | **Batch Size** (cuántos ejemplos ve antes de ajustar)               | Uno menor y uno mayor que el predeterminado                              | ¿Cambia la rapidez o la estabilidad del entrenamiento? ¿Cambia la precisión?        |
| 4   | **Cantidad de datos** (no está en Advanced, pero conviene probarlo) | 5 imágenes por clase contra 25 por clase, con los demás ajustes iguales  | ¿Qué cambia más: los ajustes avanzados o la cantidad de datos?                      |

### Tabla de registro 

| **Canción**                                  | **SDR (dB)** | **Seguridad global %** | **Voz presencia %** | **Voz seguridad %** | **Percusión presencia %** | **Percusión seguridad %** | **Bajo presencia %** | **Bajo seguridad %** | **Guitarra presencia %** | **Guitarra seguridad %** | **Piano presencia %** | **Piano seguridad %** | **Otros presencia %** | **Otros seguridad %** |
| -------------------------------------------- | ------------ | ---------------------- | ------------------- | ------------------- | ------------------------- | ------------------------- | -------------------- | -------------------- | ------------------------ | ------------------------ | --------------------- | --------------------- | --------------------- | --------------------- |
| Changing Seasons -Reload-                    | -3.3         | 76.7                   | 70.6                | 97.4                | 97.4                      | 99.5                      | 84.0                 | 99.6                 | 7.7                      | 88.4                     | 83.0                  | 96.6                  | 87.1                  | 93.8                  |
| Queen - Killer Queen (Top Of The Pops, 1974) | -2.8         | 76.7                   | 78.0                | 96.8                | 77.0                      | 97.1                      | 79.1                 | 96.6                 | 77.0                     | 92.8                     | 3.7                   | 97.3                  | 8.4                   | 94.3                  |

Aquí tienes ambas tablas en formato Markdown:

### Killer queen - queen

|**Instrumento**|**Presencia %**|**Ventanas ambiguas %**|**Posible fuga %**|**Seguridad %**|
|---|---|---|---|---|
|Voz|78.0|2.6|0.0|96.8|
|Percusión|77.0|3.1|0.0|97.1|
|Bajo|79.1|3.1|0.0|96.6|
|Guitarra|77.0|8.9|0.0|92.8|
|Piano|3.7|4.2|0.0|97.3|
|Otros|8.4|9.9|0.0|94.3|

### Changing seasons - Azumi Takahashi

|**Instrumento**|**Presencia %**|**Ventanas ambiguas %**|**Posible fuga %**|**Seguridad %**|
|---|---|---|---|---|
|Voz|70.6|4.1|0.0|97.4|
|Percusión|97.4|0.5|0.0|99.5|
|Bajo|84.0|0.5|0.0|99.6|
|Guitarra|7.7|6.7|6.7|88.4|
|Piano|83.0|3.6|0.6|96.6|

---

## 6. Preguntas para responder en la entrega

#### Utilizando killer queen de referencia*
### 1. ¿Qué instrumento estuvo más y menos presente?

El más presente fue el **bajo** con 79.1% del tiempo y el menos presente fue el **piano** con 3.7%. La voz (78.0%), la percusión (77.0%) y la guitarra (77.0%) quedaron casi iguales, lo que indica que tocan juntos durante la mayor parte de la canción. El 21-23% restante corresponde probablemente a la intro, interludios y el final.

El 3.7% del piano debe tomarse con cuidado: en la grabación de estudio de _Killer Queen_ el piano es un instrumento central, así que ese porcentaje parece demasiado bajo. Lo comento en las preguntas 7 y 8.

### 2. ¿Qué stem tuvo mayor y menor seguridad? ¿Por qué?

Mayor piano
Menor guitarra
Como la fuga fue 0.0% en todos los stems, las diferencias de seguridad vienen solo de las ventanas ambiguas, es decir, segundos cuyo volumen estuvo cerca del umbral de -40 dB. Los dos stems con menos seguridad, **Guitarra** (92.8%) y **Otros** (94.3%), son también los que tienen más ventanas ambiguas (8.9% y 9.9%). La guitarra suele alternar entre pasajes suaves y fuertes (acordes, solos, armonías), por eso cruza más veces la zona de duda.

### 3. ¿Qué tan bien se reconstruye la canción original?

El SDR fue de **-2.8 dB**, un valor negativo: significa que la diferencia entre la canción original y la suma de los 6 stems tiene más energía que la propia canción. Tomado literalmente, indicaría una reconstrucción mala. Sin embargo, creo que se debe más a cómo se mide que a la separación en sí: mi cálculo compara las ondas directamente y no compensa diferencias de volumen o de alineación. Demucs reescala el audio de salida para evitar saturación, y una pequeña diferencia de ganancia basta para volver el SDR negativo, aunque los stems suenen bien. Lo apropiado es reportarlo como “reconstrucción deficiente según esta métrica, probablemente por diferencias de escala”, y no como prueba de que la separación falló.

### 3b. ¿Qué significa la seguridad global de 76.7%?

El promedio de seguridad de los 6 stems es 95.8%, y la global se calcula como 80% de ese promedio más 20% del puntaje de reconstrucción. Como el SDR fue negativo, el puntaje de reconstrucción quedó en 0%, así que la global es simplemente 0.8 × 95.8 ≈ 76.7%. Es decir, **la reconstrucción restó unos 19 puntos**: sin esa penalización, la separación se vería casi como el 95.8% de los stems. Sigue siendo una estimación de qué tan limpia fue la separación, no una probabilidad de acierto real.

### 4. ¿Alta seguridad significa que el instrumento está bien detectado?

No. La seguridad mide qué tan **claras** fueron las decisiones de “suena / no suena”, no si son correctas. El piano tuvo la seguridad más alta (97.3%) con solo 3.7% de presencia: el sistema está muy seguro de que casi nunca suena, pero eso no confirma que realmente casi nunca suene. Por eso hay que leer presencia y seguridad juntas y contrastarlas con lo que se escucha.

### 5. ¿Qué stem tuvo más posible fuga y qué implica?

Ninguno: la fuga fue **0.0%** en los seis stems. Pero esto solo significa que ninguna ventana activa estuvo más de 25 dB por debajo del stem más fuerte. La métrica detecta fuga muy suave comparada con el resto, no una contaminación de volumen parecido, como un instrumento completo asignado al stem equivocado. Por eso 0.0% no demuestra que la separación esté libre de errores.

### 6. ¿Qué tan sensible es el resultado al umbral de silencio?

Los más sensibles son **Otros** (9.9% de ventanas ambiguas) y **Guitarra** (8.9%): al mover el umbral de -40 dB, su presencia cambiaría más. Los más estables son **Voz** (2.6%), **Percusión** y **Bajo** (3.1% cada uno), porque casi todos sus segundos están claramente por encima o por debajo del umbral.

### 7. ¿Qué error sería peor: falso positivo o falso negativo?

Para estadísticas de presencia, el **falso positivo** es peor, porque infla el porcentaje de un instrumento sin que se note. Aquí el riesgo se ve en la guitarra: si el 77.0% incluye piano mal asignado, sería un caso de falso positivo, y al mismo tiempo el piano tendría falsos negativos (3.7%). Para aislar una pista (karaoke, por ejemplo), sería peor el falso negativo, porque se perdería audio real del instrumento.

### 9. ¿Confiarías en este sistema para usarlo en la vida real? ¿Qué le falta?

Si pero solo de manera educativa o recreativa ya que no tiene demasiada fidelidad ni veracidad lo cual no es lo más eficiente para un uso comercial o en alguna cosa de suma importancia.


---

## 8. Dato extra

-El proyecto, sus resultados y las canciones usadas se encontraran en el repositorio de github
