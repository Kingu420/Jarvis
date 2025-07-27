async function sendCommand() {
  const command = document.getElementById("commandInput").value;
  if (!command) return;

  const res = await fetch("http://127.0.0.1:5000/process", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ command })
  });

  const data = await res.json();
  document.getElementById("response").innerText = data.response;
}
