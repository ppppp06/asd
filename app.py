import subprocess
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def redireccionar_salida():
    proceso = subprocess.Popen(["python", "start.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    for linea in proceso.stdout:
        mostrar_mensaje(linea)
    for linea in proceso.stderr:
        mostrar_mensaje(linea) 

def mostrar_mensaje(mensaje):
    texto_terminal.insert(tk.END, mensaje)
    texto_terminal.see(tk.END)

app = tk.Tk()
app.title("Aplicación con Terminal")
app.geometry("800x600")

boton_iniciar = tk.Button(app, text="Iniciar", command=redireccionar_salida)
boton_iniciar.pack()

texto_terminal = ScrolledText(app, wrap=tk.WORD)
texto_terminal.pack(expand=True, fill="both")

app.mainloop()
