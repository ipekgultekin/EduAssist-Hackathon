from fastapi import APIRouter
from models.schemas import EducationRequest
import os
import requests
from dotenv import load_dotenv
from fastapi import UploadFile, File
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
        return {"response": result["candidates"][0]["content"]["parts"][0]["text"]}
    except:
        return {"error": "AI response error", "raw": result}



@router.post("/image-question")
async def solve_image_question(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

        prompt = {
            "contents": [
                {
                    "parts": [
                        {
                            "inline_data": {
                                "mime_type": file.content_type,
                                "data": base64_image
                            }
                        },
                        {
                            "text": "Bu görseldeki soruyu detaylıca çöz ve açıklamalı anlat. Türkçe cevapla."
                        }
                    ]
                }
            ]
        }

        response = requests.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent",
            headers={"Content-Type": "application/json"},
            params={"key": GEMINI_API_KEY},
            json=prompt
        )

        result = response.json()
        print("Gemini response:", result)

        try:
            return {"response": result["candidates"][0]["content"]["parts"][0]["text"]}
        except:
            return {"error": "AI cevabı alınamadı", "raw": result}

    except Exception as e:
        return {"error": str(e)}