from PIL import ImageGrab
import time

time.sleep(3)

# Coordenadas del área que deseas capturar
x1, y1, x2, y2 = 1790, 990, 1827, 1006

# Tomar una captura de pantalla del área especificada
captura_pantalla = ImageGrab.grab(bbox=(x1, y1, x2, y2))

# Guardar la captura de pantalla en un archivo (opcional)
captura_pantalla.save("captura.png")

# Para mostrar la captura de pantalla (opcional)
captura_pantalla.show()