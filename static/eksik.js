document.getElementById("eksik-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const topic = document.getElementById("topic").value;
    const lang = document.getElementById("lang").value;

    const payload = {
        topic: topic,
        lang: lang,
        mode: "eksik_tespit"
    };

    sendAIRequest("/educational-ai", payload, "ai-result");
});
