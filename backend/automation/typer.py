import pyautogui
import time

def type_code(code: str):
    time.sleep(2)  # Give time to focus the editor
    pyautogui.write(code, interval=0.02)
