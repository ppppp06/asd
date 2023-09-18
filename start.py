import pyautogui
import time
import subprocess

time.sleep(1)

pyautogui.keyDown('8')
time.sleep(0.1) 
pyautogui.keyUp('8')  

time.sleep(0.1)  

pyautogui.keyDown('shift')
time.sleep(0.1)  
pyautogui.keyUp('shift') 

time.sleep(0.1)

pyautogui.keyDown('F5')
time.sleep(0.05)  
pyautogui.keyUp('F5')

subprocess.run(["python", "verification.py"]) 