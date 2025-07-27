document.addEventListener("DOMContentLoaded", () => {
    const submitBtn = document.querySelector("form button[type='submit']");
    if (submitBtn) {
        submitBtn.dataset.originalText = submitBtn.innerText;
    }
});

async function sendAIRequest(endpoint, payload, resultContainerId) {
    const resultEl = document.getElementById(resultContainerId);
    const submitBtn = document.querySelector("form button[type='submit']");

    try {
        submitBtn.disabled = true;
        submitBtn.innerText = "🌀 Cevap bekleniyor...";
        resultEl.innerText = "Yapay zekâ hazırlanıyor...";

        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (data.response) {
            resultEl.innerHTML = marked.parse(data.response); // Markdown desteği
        } else {
            resultEl.innerText = "Hata: " + (data.error || "Bilinmeyen bir sorun oluştu.");
            console.error("Raw:", data.raw);
        }
    } catch (error) {
        console.error("Error:", error);
        resultEl.innerText = "İstek başarısız oldu.";
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerText = submitBtn.dataset.originalText || "Gönder";
    }
}
