from flask import Flask, request, jsonify
from flask_cors import CORS
from logic.command_handler import handle_custom_command  # Your Jarvis logic

app = Flask(__name__)
CORS(app)  # Enable requests from frontend

@app.route('/process', methods=['POST'])
def process_command():
    data = request.get_json()
    command = data.get('command', '')
    print(f"Received: {command}")

    # Simulate processing
    response = "Sorry, I didn’t understand."  # default fallback

    # Use your handler
    if handle_custom_command(command):
        response = f"Handled command: {command}"
    else:
        response = f"I don't know how to '{command}' yet."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
