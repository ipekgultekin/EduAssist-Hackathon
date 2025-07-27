document.getElementById("topic-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const topic = document.getElementById("topic").value;
    const lang = document.getElementById("lang").value;

    const payload = {
        topic: topic,
        lang: lang,
        mode: "konu_anlatimi"
    };

    sendAIRequest("/educational-ai", payload, "ai-result");
});
