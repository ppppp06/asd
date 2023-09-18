import subprocess
import pyautogui
import time

# Leer el contenido del archivo para depuración
with open("estado_ez.txt", "r") as f:
    archivo_contenido = f.read()

# Convertir el contenido del archivo a booleano
ez = archivo_contenido.strip().lower() == "true"

try:
    # Verificar si "ez" está en alguna de las salidas
    if ez:
        print("Se ejecutó correctamente ez.")

        # Borrar el "True" del estado_ez.txt y escribir "False"
        with open("estado_ez.txt", "w") as f:
            f.write("False")

        pyautogui.keyDown('F9')
        time.sleep(0.05)
        pyautogui.keyUp('F9')

        time.sleep(40)

        pyautogui.keyDown('F5')
        time.sleep(0.05)
        pyautogui.keyUp('F5')

        subprocess.run(["python", "verification.py"])
    else:
        print("Ya no se está ejecutando ez.")
        # Agregar aquí las acciones que deseas realizar cuando no se detecta "ez"
except subprocess.CalledProcessError as e:
    # Capturar errores si los comandos fallan
    print("Error al ejecutar los comandos:", e)
