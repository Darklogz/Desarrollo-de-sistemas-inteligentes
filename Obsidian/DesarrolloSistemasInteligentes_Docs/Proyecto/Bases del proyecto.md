
## Leonardo Alejandro Mondragón Morales
### Comunicación para definir el proyecto
Crear un sistema con una red neuronal cuyo propósito sea el de interpretar al usuario y poder asistirlo en sus labores diarias en el uso de una computadora, por medio de voz y detección de imágenes y lector de procesos será como lo que Siri o Cortana no son capaces de hacer

Lista de deseos:
- Que escuche y entienda la voz
- Que pueda ver y leer la pantalla
- Que tenga acceso al teclado
- Que sea lo más ligero posible

---
### **Requerimientos Funcionales (RF)**

1. **Reconocimiento y captura de voz (STT):** El sistema debe escuchar el micrófono del usuario y convertir los comandos de voz a texto en español en tiempo real.
2. **Ejecución de acciones del sistema:** El sistema debe ser capaz de abrir y cerrar aplicaciones, controlar ventanas y realizar acciones del sistema operativo Windows mediante órdenes habladas.
3. **Dictado por voz:** El sistema debe permitir ingresar texto mediante dictado de voz e insertarlo de forma automática en el campo activo de cualquier ventana de Windows.
4. **Búsqueda e investigación web:** El sistema debe realizar búsquedas automáticas en internet ante consultas complejas, extraer la información de las páginas resultantes y generar un resumen sintético.
5. **Lectura y comprensión de pantalla (OCR):** El sistema debe capturar el contenido visual de la pantalla a petición del usuario para leer texto presente en imágenes o responder preguntas sobre lo que se muestra.
6. **Respuesta mediante síntesis de voz (TTS):** El sistema debe responder de forma hablada en español confirmando la realización de acciones o comunicando las respuestas a las investigaciones.
7. **Enrutamiento e interpretación de intenciones:** El sistema debe utilizar un modelo de lenguaje local para interpretar el comando e inferir automáticamente si requiere una acción en el sistema host, un dictado, una lectura de pantalla o una búsqueda en la web.

---
### **Requerimientos No Funcionales (RNF)**

1. **Tiempo de respuesta en acciones locales:** Las órdenes simples de control del sistema y dictado deben procesarse y ejecutarse en **menos de 5 a 15 segundos**.
2. **Tiempo de respuesta en investigaciones:** Las consultas complejas que requieran búsqueda web y resumen de información no deben superar **1 minuto** de tiempo total de respuesta.
3. **Límite de consumo de memoria RAM:** El consumo máximo combinado de los contenedores Docker y servicios de IA no debe sobrepasar **6 GB de RAM**, garantizando que queden al menos 10 GB libres para el sistema operativo Windows y el uso diario.
4. **Compatibilidad con hardware sin GPU dedicada:** Todo el pipeline de modelos (STT, LLM, TTS, OCR) debe ejecutar sus inferencias optimizadas para procesar eficientemente en la **CPU Intel Core i5 e iGPU Intel Iris Xe**.
5. **Privacidad y procesamiento local:** La captura de audio, la transcripción, la síntesis de voz y la interpretación de comandos deben procesarse **100% de forma local** sin enviar datos sensibles a servicios de terceros en la nube.
6. **Arquitectura desacoplada (Docker + Host):** Los servicios pesados de IA deben estar aislados en contenedores Docker, mientras que la ejecución de comandos del SO se realiza mediante un agente ligero en la máquina host de Windows.
7. **Estabilidad y tolerancia a fallos:** El sistema debe interceptar y gestionar errores de ejecuciones o búsquedas sin provocar el congelamiento (_lag_) o colapso (_crash_) de la laptop ni de la máquina virtual de Docker/WSL2.

---
Diagrama de casos de uso
![[Pasted image 20261118160700.png]]

---
Diagrama de uso
![[Pasted image 20261118160118.png]]

---
Diagrama de clases

![[Pasted image 20261118161258.png]]

--- 
Arquitectura del sistema
## Tecnologías del proyecto

**Lenguaje y servicios**

- Python 3.11+
- FastAPI + Uvicorn (API del Núcleo IA)
- httpx (comunicación Host ↔ Núcleo)

**Inteligencia artificial**

- faster-whisper, modelo `base` o `tiny` en INT8 (voz a texto)
- Ollama con Qwen2.5-3B-Instruct Q4 (LLM)
- Piper TTS con voz en español (texto a voz)
- RapidOCR (lectura de pantalla)
- Silero VAD o webrtcvad (detección de silencio)
- openWakeWord (palabra de activación, opcional)

**Búsqueda web**

- duckduckgo-search
- BeautifulSoup4

**Agente Host (control del sistema)**

- pyautogui (teclado y mouse)
- pynput (atajo global)
- pyperclip (portapapeles)
- subprocess y psutil (abrir/cerrar apps y procesos)
- mss (captura de pantalla)
- sounddevice (micrófono y reproducción de audio)

**Mascota e interfaz**

- PySide6 o Tkinter (ventana transparente sin bordes con PNG y burbuja)
- Pillow (manejo de los PNG)

**Específico de Linux**

- xdotool (X11) o wtype / ydotool (Wayland) para insertar texto

**Contenedores y despliegue**

- Docker Desktop + Docker Compose (Windows)
- WSL2 con `.wslconfig` para limitar la RAM
- Scripts `iniciar.bat` (Windows) e `iniciar.sh` (Linux)
- venv de Python (Linux)

**Configuración y utilidades**

- PyYAML (archivo `config.yaml`)
- logging de Python (registro de errores)