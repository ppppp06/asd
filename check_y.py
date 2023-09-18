from PIL import ImageGrab
import pytesseract
import time
import subprocess
import pyautogui

x1, y1, x2, y2 = 1791, 1010, 1815, 1026

captura_pantalla_y1 = ImageGrab.grab(bbox=(x1, y1, x2, y2))

config = '--psm 6' 

texto_captura_y1 = pytesseract.image_to_string(captura_pantalla_y1, config=config)

numero_deseado = "67"

if numero_deseado in texto_captura_y1:
    print(f"Y {numero_deseado} está bien.")
else:
    print(f"Y {numero_deseado} está mal. 1/2")
    time.sleep(2)
    
    # Comprueba nuevamente después de un tiempo
    captura_pantalla_y2 = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    texto_captura_y2 = pytesseract.image_to_string(captura_pantalla_y2, config=config)
    
    if texto_captura_y1 == texto_captura_y2:
        print(f"Y {numero_deseado} está mal. 2/2")
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
