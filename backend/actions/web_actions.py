import webbrowser
from logic.speaker import speak

def open_youtube():
    speak("Opening YouTube.")
    webbrowser.open("https://www.youtube.com")

def search_google(query=None):
    if not query:
        speak("What should I search on Google?")
        return
    speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def search_github(query=None):
    if not query:
        speak("What should I search on GitHub?")
        return
    speak(f"Searching GitHub for {query}")
    webbrowser.open(f"https://github.com/search?q={query}")
