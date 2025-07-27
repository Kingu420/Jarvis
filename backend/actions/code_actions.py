from logic.speaker import speak
from automation.typer import type_code

def generate_function(command: str):
    command = command.lower()

    if "add two numbers" in command:
        code = """def add(a, b):\n    return a + b"""
        speak("Here's a function that adds two numbers.")
        type_code(code)

    elif "reverse a string" in command:
        code = """def reverse_string(s):\n    return s[::-1]"""
        speak("Here's a function to reverse a string.")
        type_code(code)

    elif "student class" in command or "class for a student" in command:
        code = (
            "class Student:\n"
            "    def __init__(self, name, roll):\n"
            "        self.name = name\n"
            "        self.roll = roll\n\n"
            "    def display(self):\n"
            "        print(f\"Name: {self.name}, Roll: {self.roll}\")"
        )
        speak("Here is a student class in Python.")
        type_code(code)

    else:
        speak("Sorry, I can't generate code for that yet.")
