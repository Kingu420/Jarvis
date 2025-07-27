import speech_recognition as sr

recognizer = sr.Recognizer()

# Check microphone index
for i, mic in enumerate(sr.Microphone.list_microphone_names()):
    print(f"{i}: {mic}")
