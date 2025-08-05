document.getElementById("topic-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const topic = document.getElementById("topic").value;
    const lang = document.getElementById("lang").value;

    const payload = {
    topic: topic,
    lang: lang,
    mode: "konu_anlatimi",
    question: "",
    step: 0,
    answer: ""
};


    sendAIRequest("/educational-ai", payload, "ai-result");
});
