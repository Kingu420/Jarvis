import json
from logic.speaker import speak
from actions import system_actions, web_actions, info_actions

def load_commands():
    with open("data/commands.json", "r") as file:
        return json.load(file)

def handle_custom_command(command: str):
    command = command.lower()
    all_cmds = load_commands()
    
    for category in ["greetings", "apps", "search", "learned"]:
        if command in all_cmds.get(category, {}):
            response = all_cmds[category][command]

            if response.startswith("say:"):
                speak(response.split("say:")[1])
                return True

            elif response.startswith("open_app:"):
                app = response.split("open_app:")[1]
                system_actions.open_app(app)
                return True

            elif response.startswith("google:"):
                web_actions.search_google(response.split("google:")[1])
                return True

            elif response.startswith("wiki:"):
                info_actions.search_wikipedia(response.split("wiki:")[1])
                return True

            elif response.startswith("github:"):
                web_actions.search_github(response.split("github:")[1])
                return True

            else:
                speak(response)
                return True

    return False  # Only reached if no category matched


def learn_new_command(command):
    speak(f"I don't understand '{command}'. What should I do when you say that?")
    print(">>> Type response in format like:")
    print("    say:Hello there!")
    print("    open_app:notepad")
    print("    wiki:Python")
    action = input("Your response: ").strip()

    if not action:
        speak("Okay, I won't save anything.")
        return

    all_cmds = load_commands()
    all_cmds.setdefault("learned", {})[command] = action

    with open("data/commands.json", "w") as file:
        json.dump(all_cmds, file, indent=2)

    speak("Got it! I’ve learned something new.")
