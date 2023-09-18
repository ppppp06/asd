from PIL import ImageGrab
import pytesseract
import time
import subprocess
import pyautogui

x1, y1, x2, y2 = 1790, 990, 1827, 1006

captura_pantalla_x1 = ImageGrab.grab(bbox=(x1, y1, x2, y2))

config = '--psm 6' 

texto_captura_x1 = pytesseract.image_to_string(captura_pantalla_x1, config=config)

time.sleep(1)

captura_pantalla_x2 = ImageGrab.grab(bbox=(x1, y1, x2, y2))

texto_captura_x2 = pytesseract.image_to_string(captura_pantalla_x2, config=config)

if texto_captura_x1 != texto_captura_x2:
    print("X está bien.")
else:
    print("X está mal. 1/2")
    time.sleep(3)
    
    # Comprueba nuevamente después de un tiempo
    captura_pantalla_x3 = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    texto_captura_x3 = pytesseract.image_to_string(captura_pantalla_x3, config=config)
    
    if texto_captura_x2 == texto_captura_x3:
        print("X está mal. 2/2")
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
