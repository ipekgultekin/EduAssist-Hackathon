from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import JSONResponse
import os
import requests
from dotenv import load_dotenv
import base64

load_dotenv()
router = APIRouter()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@router.post("/educational-ai")
async def educational_response(request: Request):
    data = await request.json()
    topic = data.get("topic", "")
    lang = data.get("lang", "Türkçe")
    mode = data.get("mode", "")

    question = data.get("question")
    step = data.get("step", 0)
    answer = data.get("answer")

    if mode == "konu_anlatimi":
        prompt = f"{topic} konusunu sade ve anlaşılır bir şekilde açıkla. Lütfen {lang} dilinde yaz."

    elif mode == "soru_cozumu":
        prompt = f"Soru: {question}\nKonu: {topic}\nLütfen adım adım çözümünü {lang} dilinde yaz."

    elif mode == "eksik_tespit":
        prompt = f"{topic} konusuyla ilgili bana birkaç zorlayıcı soru sor. Benim cevaplarıma göre eksiklerimi tespit et. Cevapları {lang} dilinde ver."

    elif mode == "get_question":
        prompt = f"{lang} dilinde, {topic} konusunda öğrencinin konuyu anlayıp anlamadığını ölçen {step + 1}. sıradaki zorlayıcı bir soru yaz. Yalnızca soruyu ver."

    elif mode == "eduplan":
        prompt = f"Kullanıcının hedefi şu: {topic}. Bu hedefe yönelik detaylı, sade ve hedefe yönelik bir ders çalışma planı hazırla. Cevabı {lang} dilinde ver."

    elif mode == "eksik_test":
        prompt = (
            f"{topic} konusu\nSoru {step + 1}: {question}\n"
            f"Öğrencinin cevabı: {answer}\n"
            f"Cevabı değerlendir. Format:\n"
            f"Doğru/Yanlış: ...\nAçıklama: ...\nDil: {lang}"
        )


    else:
        return {"error": "Geçersiz mod"}

    response = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent",
        headers={"Content-Type": "application/json"},
        params={"key": GEMINI_API_KEY},
        json={"contents": [{"parts": [{"text": prompt}]}]}
    )

    result = response.json()
    print("MODE:", mode)
    print("PROMPT:", prompt)
    print("RESPONSE:", result)

    try:
        candidates = result.get("candidates")
        if not candidates:
            raise ValueError("Gemini API yanıtında candidates yok")

        content = candidates[0].get("content", {})
        parts = content.get("parts", [])
        if not parts:
            raise ValueError("Gemini API yanıtında content.parts yok")

        ai_text = parts[0].get("text", "")
        if not ai_text:
            raise ValueError("AI cevabı boş döndü")

        if mode == "eksik_test":
            lines = ai_text.strip().split("\n")
            correctness_line = lines[0].lower()
            explanation = "\n".join(lines[1:]).strip()
            is_correct = "doğru" in correctness_line and "yanlış" not in correctness_line
            return {
                "correct": is_correct,
                "feedback": explanation if explanation else ai_text
            }

        elif mode == "get_question":
            return {"question": ai_text}

        else:
            return {"solution": ai_text}

    except Exception as e:
        print("Gemini parse hatası:", e)
        return {
            "error": "AI response error",
            "raw": result
        }

@router.post("/image-question")
async def solve_image_question(photo: UploadFile = File(...)):
    image_bytes = await photo.read()
    encoded_image = base64.b64encode(image_bytes).decode('utf-8')

    headers = {
        "Content-Type": "application/json"
    }

    params = {
        "key": GEMINI_API_KEY
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": photo.content_type,
                            "data": encoded_image
                        }
                    },
                    {
                        "text": "Bu görseldeki soruyu çöz ve detaylı bir şekilde açıklayıcı cevap ver. Türkçe yaz."
                    }
                ]
            }
        ]
    }

    response = requests.post(
        "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent",
        headers=headers,
        params=params,
        json=payload
    )

    result = response.json()
    print("Gemini image response:", result)

    try:
        ai_text = result["candidates"][0]["content"]["parts"][0]["text"]
        return {"success": True, "solution": ai_text}
    except Exception as e:
        print("AI çözüm parse edilemedi:", e)
        return {
            "success": False,
            "error": "AI response error",
            "raw": result
        }
