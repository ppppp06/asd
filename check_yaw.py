from PIL import ImageGrab
import pytesseract
import time
import subprocess
import pyautogui

x1, y1, x2, y2 = 55, 31, 80, 49

captura_pantalla_yaw1 = ImageGrab.grab(bbox=(x1, y1, x2, y2))

config = '--psm 6'

texto_captura_yaw1 = pytesseract.image_to_string(captura_pantalla_yaw1, config=config)

numero_deseado = "18"

if numero_deseado in texto_captura_yaw1:
    print(f"Yaw 180 está bien.")
else:
    print(f"Yaw 180 está mal. 1/2")
    time.sleep(2)
    
    # Comprueba nuevamente después de un tiempo
    captura_pantalla_yaw2 = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    texto_captura_yaw2 = pytesseract.image_to_string(captura_pantalla_yaw2, config=config)
    
    if texto_captura_yaw1 == texto_captura_yaw2:
        print(f"Yaw 180 está mal. 2/2")
        # Desactiva 'activo' y ejecuta las acciones adicionales
        activo = False
        time.sleep(0.25) 

        pyautogui.keyDown('F7')
        time.sleep(0.05)  
        pyautogui.keyUp('F7')

        time.sleep(0.5)  

        pyautogui.keyDown('F7')
        time.sleep(0.05)  
        pyautogui.keyUp('F7') 

        time.sleep(0.5)  
        
        with open("estado_ez.txt", "w") as f:
            f.write("True")

        subprocess.run(["python", "ez.py"])
