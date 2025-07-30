from fastapi import APIRouter, UploadFile, File
from models.schemas import EducationRequest
from fastapi.responses import JSONResponse
import os
import requests
from dotenv import load_dotenv
import base64

load_dotenv()
router = APIRouter()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@router.post("/educational-ai")
def educational_response(data: EducationRequest):
    if data.mode == "konu_anlatimi":
        prompt = f"Lütfen {data.topic} konusunu detaylı ama sade bir şekilde anlat. Cevabı {data.lang} dilinde ver."

    elif data.mode == "soru_cozumu":
        prompt = f"{data.question} sorusunu detaylı bir şekilde çöz ve açıklamalar yap. Konu: {data.topic}. Cevabı {data.lang} dilinde ver."

    elif data.mode == "eksik_tespit":
        prompt = f"{data.topic} konusuyla ilgili bana birkaç zorlayıcı soru sor. Benim cevaplarıma göre eksiklerimi tespit et. Cevapları {data.lang} dilinde ver."

    elif data.mode == "get_question":
        prompt = f"{data.topic} konusuyla ilgili {data.step + 1}. sıradaki anlamayı ölçen zorlayıcı tek bir soru sor. Sadece soruyu ver. {data.lang} dilinde sor."

    elif data.mode == "eksik_test":
        prompt = (
            f"Aşağıda {data.topic} konusuyla ilgili {data.step + 1}. soru var. "
            f"Kullanıcının verdiği cevap da altında. Bu cevabı değerlendir. "
            f"Aşağıdaki formatta çok kısa cevap ver:\n"
            f"Doğru/Yanlış: [Doğru ya da Yanlış yaz]\n"
            f"Açıklama: [Kısa açıklama yap]\n\n"
            f"Soru: {data.question}\nCevap: {data.answer}\nDil: {data.lang}"
        )

    else:
        return {"error": "Invalid mode"}

    response = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent",
        headers={"Content-Type": "application/json"},
        params={"key": GEMINI_API_KEY},
        json={"contents": [{"parts": [{"text": prompt}]}]}
    )

    result = response.json()

    try:
        ai_text = result["candidates"][0]["content"]["parts"][0]["text"]

        if data.mode == "eksik_test":
            lines = ai_text.strip().split("\n")
            correctness_line = lines[0].lower()
            explanation = "\n".join(lines[1:]).strip()

            is_correct = "doğru" in correctness_line and "yanlış" not in correctness_line

            return {
                "correct": is_correct,
                "feedback": explanation if explanation else ai_text
            }

        elif data.mode == "get_question":
            return {"question": ai_text}

        else:
            return {"response": ai_text}

    except Exception as e:
        return {"error": "AI response error", "raw": result}


@router.post("/image-question")
async def solve_image_question(photo: UploadFile = File(...)):
    # Görseli oku ve base64'e çevir
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
    print("Gemini response:", result)  # 🔍 buraya eklenecek

    try:
        ai_text = result["candidates"][0]["content"]["parts"][0]["text"]
        return {"success": True, "solution": ai_text}
    except Exception as e:
        print("AI çözüm parse edilemedi:", e)
        print("Orijinal Gemini sonucu:", result)
        return {
            "success": False,
            "error": "AI response error",
            "raw": result
        }

