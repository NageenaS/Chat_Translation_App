// Handle Message Form Submission
document.getElementById("messageForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const sender = document.getElementById("sender").value;
    const recipient = document.getElementById("recipient").value;
    const message = document.getElementById("message").value;

    const response = await fetch("/send-message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sender, recipient, message })
    });
    const result = await response.json();
    document.getElementById("result").innerText = JSON.stringify(result, null, 2);
});

// Handle Preferences Form Submission
document.getElementById("preferencesForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const user = document.getElementById("user").value;
    const preferred_language = document.getElementById("preferred_language").value;
    const tone = document.getElementById("tone").value;

    const response = await fetch("/update-preferences", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user, preferred_language, tone })
    });
    const result = await response.json();
    document.getElementById("response").innerText = result.message;
});
