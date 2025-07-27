import wikipedia
from logic.speaker import speak

def search_wikipedia(query):
    speak(f"Searching Wikipedia for {query}")
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia...")
        speak(summary)
    except Exception:
        speak("Sorry, I couldn't find that.")
