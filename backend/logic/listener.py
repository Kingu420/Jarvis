import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        print("🧠 Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f">> You said: {query}")
        return query.lower()

    except sr.WaitTimeoutError:
        print("⏳ Listening timed out. Try again.")
        return ""

    except sr.UnknownValueError:
        print("😕 Could not understand audio.")
        return ""

    except sr.RequestError as e:
        print(f"❌ API unavailable or error occurred: {e}")
        return ""

    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user.")
        exit()
