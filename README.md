# 🧠 Documentación general del proyecto: keylogger_lab

## 📌 Objetivo

Este proyecto nace como un laboratorio de aprendizaje personal hecho originalmente por `YasminaCodes` para explorar el funcionamiento de un keylogger a bajo nivel, usando Python. Se enfoca en capturar eventos de teclado, analizarlos, documentarlos y reflexionar sobre su uso técnico y ético.

## ⚙️ Tecnologías usadas

- **Python:** para capturar eventos del sistema y escribirlos en un archivo.

- **pynput:** librería que permite escuchar las pulsaciones del teclado de forma independiente del sistema operativo.

- **Bash:** scripting básico para ejecutar el programa de manera más realista o automatizada en sistemas Unix.

## 🎯 Funciones implementadas - Que hace este proyecto

- Detección de teclas al presionarlas.
- Escritura en un archivo `keyboard-log.txt` (modo append).
- Manejo de teclas especiales (`Enter`, `Tab`, `Space`, `Backspace`, etc.).
- Simulación de retroceso con Backspace modificando directamente el archivo.
- Uso de match-case para facilitar escalabilidad de acciones según tecla detectada.
- Mecanismo de salida con la tecla `Esc`.

## 🧪 Exploraciones adicionales

- Documentación en forma de bitácora técnica personal.
- Uso de `run.sh` para simular ejecución oculta en un sistema Unix.
- Reflexión sobre cómo debería comportarse un keylogger real (ejecución al inicio del sistema, ocultamiento, segundo plano, etc.).

## ⚠️ Enfoque ético

Todo el código está destinado exclusivamente a fines educativos y de investigación técnica.
Se prohíbe expresamente su uso para espionaje, violación de la privacidad u otros fines maliciosos.

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/keylogger_lab.git
cd keylogger_lab

# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows

# Instalar dependencia principal
pip install pynput
```
## ▶ Uso basico

```bash
# Ejecutar el script en primer plano
python main.py
```
o bien, usar el script de automatizacion

```bash
bash run.sh
```
🚫 hay que pulir detalles

## 📂 Archivos importantes

|   archivo   |                         Descripcion                          |
| :---------: | :----------------------------------------------------------: |
|  `main.py`  |         Script principal del keylogger (Laboratorio)         |
|  `run.sh`   | Script bash que mueve y ejecuta el programa en segundo plano |
| `README.md` |              Documentacion general del proyecto              |

## ⚠️ Advertencia legal y ética

Este proyecto tiene fines exclusivamente educativos.
El uso de herramientas de captura de teclado fuera de entornos controlados, personales o de laboratorio puede ser ilegal y violar derechos de privacidad.
El autor no se responsabiliza por el mal uso de este código.

## 📓 Bitácora de laboratorio (hasta ahora)

| Versión | Cambio principal                       | Descripción breve                                                                |
| ------- | -------------------------------------- | -------------------------------------------------------------------------------- |
| v0.1    | Detección de teclas                    | Captura y muestra cada tecla presionada por consola.                             |
| v0.2    | Guardado en archivo `keyboard-log.txt` | Se crea/actualiza un archivo con cada tecla presionada.                          |
| v0.3    | Tecla Esc detiene el script            | Agrega mecanismo de salida segura para pruebas de laboratorio.                   |
| v0.4    | Manejo de tecla Backspace              | Simula retroceso modificando el archivo, eliminando el último carácter guardado. |
| v0.5    | Ejecución oculta con `run.sh`          | Script Bash que mueve y ejecuta el programa en `/tmp` en segundo plano.          |

## ✍️ Autor
Carlos Andres Alzate
Proyecto original basado en ideas de Jasmina Codes.
Bitácora personal de aprendizaje sobre seguridad informática, scripting y desarrollo de herramientas técnicas desde una perspectiva autodidacta.
