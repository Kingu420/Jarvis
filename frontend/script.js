const text = "Hello, I am Jarvis - your assistant";
let index = 0;

// Typewriter animation
function typeWriter() {
  if (index < text.length) {
    document.querySelector(".typewriter").textContent += text.charAt(index);
    index++;
    setTimeout(typeWriter, 100);
  }
}

window.onload = typeWriter;

// Send command handler
function sendCommand() {
  const input = document.getElementById("commandInput");
  const chatBox = document.getElementById("chat-box");
  const command = input.value.trim();

  if (!command) return;

  // Display user command
  chatBox.innerHTML += `
    <div class="alert alert-primary p-2 my-2"><strong>You:</strong> ${command}</div>
  `;
  input.value = "";

  // Send to backend (replace this block if you want real backend communication)
  fetch('http://127.0.0.1:5000/process', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ command })
  })
    .then(response => response.json())
    .then(data => {
      chatBox.innerHTML += `
        <div class="alert alert-success p-2"><strong>Jarvis:</strong> ${data.response}</div>
      `;
      chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
      chatBox.innerHTML += `
        <div class="alert alert-danger p-2"><strong>Jarvis:</strong> Failed to process your command.</div>
      `;
      console.error("❌ Error:", error);
    });
}
