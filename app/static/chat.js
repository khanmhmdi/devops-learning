async function sendMessage() {
    const input = document.getElementById("prompt");
    const chat = document.getElementById("chat");
    const message = input.value.trim();

    if (!message) return;

    // Show user message
    chat.innerHTML += `<div class="user"><b>You:</b> ${message}</div>`;
    input.value = "";

    // Send to backend
    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: message })
    });

    const data = await response.json();

    // Show bot response
    chat.innerHTML += `<div class="bot"><b>AI:</b> ${data.response}</div>`;
    chat.scrollTop = chat.scrollHeight;
}
