import os
import platform
from logic.speaker import speak

def shutdown():
    speak("Shutting down the system.")
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    else:
        os.system("sudo shutdown now")

def restart():
    speak("Restarting the system.")
    if platform.system() == "Windows":
        os.system("shutdown /r /t 1")
    else:
        os.system("sudo reboot")

def log_off():
    speak("Logging out now.")
    if platform.system() == "Windows":
        os.system("shutdown /l")
    else:
        os.system("gnome-session-quit --logout --no-prompt")

def open_app(app_name):
    speak(f"Opening {app_name}")
    if platform.system() == "Windows":
        os.system(f"start {app_name}")
    elif platform.system() == "Linux":
        os.system(f"{app_name} &")
