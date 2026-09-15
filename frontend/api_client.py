import os
import requests
from dotenv import load_dotenv

# تحميل المتغيرات من ملف .env
load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

def query_backend(question: str):
    try:
        # إرسال السؤال للـ Backend
        response = requests.post(
            f"{API_BASE_URL}/query", 
            json={"question": question},
            timeout=30 # عشان لو الرد أخد وقت
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # رسالة خطأ لو السيرفر واقع
        return {"error": f"API connection failed. Please make sure the backend is running. Details: {str(e)}"}