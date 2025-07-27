from logic.listener import listen
from logic.speaker import speak
from logic.utils import greet_user, get_time
from actions import system_actions, web_actions, info_actions, code_actions
from logic.command_handler import handle_custom_command, learn_new_command

def handle_command(command: str):
    command = command.lower()
    
    if handle_custom_command(command):
        return
    if "time" in command:
        speak(f"The current time is {get_time()}")
    elif "open youtube" in command:
        web_actions.open_youtube()
    elif "shutdown" in command:
        system_actions.shutdown()
    elif "wikipedia" in command:
        info_actions.search_wikipedia(command)
    elif "write a function" in command:
        code_actions.generate_function(command)
    else:
        speak("Sorry, I didn't understand that.")
        
    learn_new_command(command)

def main():
    greet_user()
    while True:
        command = listen()
        if command:
            handle_command(command)

if __name__ == "__main__":
    main()
