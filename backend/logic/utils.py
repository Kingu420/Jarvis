from datetime import datetime
from logic.speaker import speak

def greet_user():
    hour = datetime.now().hour
    if hour < 12:
        speak("Good morning! I'm Jarvis.")
    elif hour < 18:
        speak("Good afternoon! I'm Jarvis.")
    else:
        speak("Good evening! I'm Jarvis.")
    speak("How can I help you?")

def get_time():
    return datetime.now().strftime("%I:%M %p")
