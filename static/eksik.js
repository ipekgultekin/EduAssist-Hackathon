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
    document.getElementById("start-form").style.display = "none";
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

    try {
        const res = await fetch("/educational-ai", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await res.json();
        const feedback = document.getElementById("feedback");

        if (data.correct) {
            correctAnswers++;
            feedback.className = "feedback-box show correct";
            feedback.innerHTML = `
                <div style="margin-bottom: 10px;"><strong>✅ Doğru cevap!</strong></div>
                <div style="padding: 10px; background: rgba(0, 128, 0, 0.1); border-left: 4px solid #28a745; border-radius: 8px;">
                    ${data.feedback}
                </div>
            `;
        } else {
            incorrectAnswers++;
            feedback.className = "feedback-box show incorrect";
            feedback.innerHTML = `
                <div style="margin-bottom: 10px;"><strong>❌ Yanlış cevap</strong></div>
                <div style="padding: 10px; background: rgba(255, 0, 0, 0.05); border-left: 4px solid #dc3545; border-radius: 8px;">
                    ${data.feedback}
                </div>
            `;
        }

        currentQuestion++;
        setTimeout(async () => {
            if (currentQuestion < totalQuestions) {
                await askNextQuestion();
            } else {
                finishSession();
            }
        }, 2000);

    } catch (err) {
        console.error("Cevap gönderilirken hata oluştu:", err);
    }
});

async function askNextQuestion() {
    const payload = {
        topic: selectedTopic,
        lang: selectedLang,
        mode: "get_question",
        step: currentQuestion
    };

    try {
        const res = await fetch("/educational-ai", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });

        const data = await res.json();
        const questionBox = document.getElementById("question");

        if (data.question) {
            currentQuestionText = data.question;
            questionBox.innerText = "Soru " + (currentQuestion + 1) + ": " + currentQuestionText;
        } else {
            console.error("AI'dan soru alınamadı:", data);
            currentQuestionText = "AI şu anda soruyu üretemedi.";
            questionBox.innerText = `⚠️ Soru ${currentQuestion + 1}: ${currentQuestionText}`;
        }

        document.getElementById("user-answer").value = "";
        const feedbackBox = document.getElementById("feedback");
        feedbackBox.innerText = "";
        feedbackBox.className = "feedback-box";

        const progress = ((currentQuestion + 1) / totalQuestions) * 100;
        document.getElementById("progress-fill").style.width = progress + "%";
        document.getElementById("progress-text").innerText = `Soru ${currentQuestion + 1} / ${totalQuestions}`;
        document.getElementById("progress-container").classList.add("show");
        document.getElementById("qa-box").classList.add("show");

    } catch (error) {
        console.error("askNextQuestion() hata:", error);
        document.getElementById("question").innerText = "⚠️ AI ile bağlantı kurulamadı.";
    }
}

function finishSession() {
    document.getElementById("question").innerText = "";

    const answerBox = document.getElementById("user-answer");
    answerBox.disabled = true;
    answerBox.value = "Test tamamlandı. Cevap veremezsiniz.";
    answerBox.style.opacity = "0.6";
    answerBox.style.cursor = "not-allowed";

    document.getElementById("answer-btn").style.display = "none";

    const feedback = document.getElementById("feedback");
    const overallClass = correctAnswers >= 3 ? "correct" : "incorrect";
    feedback.className = `feedback-box show ${overallClass}`;
    feedback.innerHTML = `
        <div style="margin-bottom: 10px;">✅ Doğru: ${correctAnswers}, ❌ Yanlış: ${incorrectAnswers}</div>
        <div style="padding: 10px; background: #f8d7da; border-left: 4px solid #dc3545; border-radius: 8px;">
            🧠 Değerlendirme: ${generateFeedback()}
        </div>
    `;

    document.getElementById("summary-actions").style.display = "block";
}

function generateFeedback() {
    if (correctAnswers === 5) return "Konuya tamamen hâkimsiniz!";
    if (correctAnswers >= 3) return "Konu hakkında genel bilginiz var ama bazı eksikler var.";
    return "Bu konuyu tekrar etmeniz önerilir.";
}
