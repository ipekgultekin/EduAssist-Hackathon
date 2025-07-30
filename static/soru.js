document.getElementById("image-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const fileInput = document.getElementById("photo");
    const file = fileInput.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("photo", file);  // ✅ ALAN ADI "photo" OLMALI

    try {
        const res = await fetch("/image-question", {
            method: "POST",
            body: formData
        });

        const data = await res.json();
        const resultEl = document.getElementById("ai-result");

        if (data.success) {
            resultEl.innerHTML = marked.parse(data.solution);
        } else {
            resultEl.innerText = "Hata: " + (data.error || "Bilinmeyen bir sorun.");
        }
    } catch (err) {
        console.error(err);
        document.getElementById("ai-result").innerText = "İstek başarısız oldu.";
    }
});
