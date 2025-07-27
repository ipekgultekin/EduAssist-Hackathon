document.getElementById("image-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const fileInput = document.getElementById("photo");
    const file = fileInput.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
        const res = await fetch("/image-question", {
            method: "POST",
            body: formData
        });

        const data = await res.json();
        const resultEl = document.getElementById("image-result");

        if (data.response) {
            resultEl.innerText = data.response;
        } else {
            resultEl.innerText = "Hata: " + (data.error || "Bilinmeyen bir sorun.");
            console.error("Raw:", data.raw);
        }
    } catch (err) {
        console.error(err);
        document.getElementById("image-result").innerText = "İstek başarısız oldu.";
    }
});
