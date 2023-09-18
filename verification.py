import threading
import time
import subprocess
import os

# Variable global para controlar el estado del macro
activo = True

# Función para realizar la acción con las teclas (macro) - Segunda acción
def realizar_accion_2():
    while activo:
        os.system('cls')  # Ejecuta el comando 'cls' en la terminal de VS Code (Windows)
        subprocess.run(["python", "check_x.py"])
        subprocess.run(["python", "check_y.py"])
        subprocess.run(["python", "check_yaw.py"])
        time.sleep(2)

# Iniciar el hilo para el segundo macro
macro_thread_2 = threading.Thread(target=realizar_accion_2)
macro_thread_2.daemon = True
macro_thread_2.start()

while True:
    try:
        output_x = subprocess.check_output(["python", "check_x.py"], stderr=subprocess.STDOUT, text=True)
        output_y = subprocess.check_output(["python", "check_y.py"], stderr=subprocess.STDOUT, text=True)
        output_yaw = subprocess.check_output(["python", "check_yaw.py"], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output_x = e.output
        output_y = e.output
        output_yaw = e.output

    time.sleep(1)
