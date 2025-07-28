let currentQuestion = 0;
let totalQuestions = 5;
let correctAnswers = 0;
let incorrectAnswers = 0;
let selectedTopic = "";
let selectedLang = "";
let currentQuestionText = "";

document.getElementById("eksik-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    selectedTopic = document.getElementById("topic").value;
    selectedLang = document.getElementById("lang").value;
    document.getElementById("qa-box").style.display = "block";
    document.getElementById("eksik-form").style.display = "none";
    await askNextQuestion();
});

document.getElementById("answer-btn").addEventListener("click", async function () {
    const userAnswer = document.getElementById("user-answer").value;
    if (!userAnswer) return;

    const payload = {
        topic: selectedTopic,
        lang: selectedLang,
        mode: "eksik_test",
        step: currentQuestion,
        answer: userAnswer,
        question: currentQuestionText
    };

    const res = await fetch("/educational-ai", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    const data = await res.json();
    const feedback = document.getElementById("feedback");

    if (data.correct) {
        correctAnswers++;
        feedback.innerText = "✅ Doğru: " + data.feedback;
    } else {
        incorrectAnswers++;
        feedback.innerText = "❌ Yanlış: " + data.feedback;
    }

    currentQuestion++;
    setTimeout(async () => {
        if (currentQuestion < totalQuestions) {
            await askNextQuestion();
        } else {
            finishSession();
        }
    }, 2000);
});

async function askNextQuestion() {
    const payload = {
        topic: selectedTopic,
        lang: selectedLang,
        mode: "get_question",
        step: currentQuestion
    };

    const res = await fetch("/educational-ai", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    const data = await res.json();
    currentQuestionText = data.question;
    document.getElementById("question").innerText = "Soru " + (currentQuestion + 1) + ": " + currentQuestionText;
    document.getElementById("user-answer").value = "";
    document.getElementById("feedback").innerText = "";
}

function finishSession() {
    document.getElementById("question").innerText = "";
    document.getElementById("user-answer").style.display = "none";
    document.getElementById("answer-btn").style.display = "none";
    document.getElementById("feedback").innerHTML =
        `✅ Doğru: ${correctAnswers}, ❌ Yanlış: ${incorrectAnswers}<br>` +
        `🧠 Değerlendirme: ${generateFeedback()}`;

    // Artık result-box yok, hata engellendi
    // document.getElementById("result-box").style.display = "none";

    // Ana sayfa butonunu göster
    document.getElementById("summary-actions").style.display = "block";
}

function generateFeedback() {
    if (correctAnswers === 5) return "Konuya tamamen hâkimsiniz!";
    if (correctAnswers >= 3) return "Konu hakkında genel bilginiz var ama bazı eksikler var.";
    return "Bu konuyu tekrar etmeniz önerilir.";
}
