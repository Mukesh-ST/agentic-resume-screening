from groq import Groq
from dotenv import load_dotenv
import os
from app.prompts import EXTRACT_JD_DETAILS
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_jd(text: str) -> str:
    """
    Function to analyze the extracted text from a job description using Groq's API.
    """
    prompt = EXTRACT_JD_DETAILS.format(jd_text=text)
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        print("Response from Groq API for JD:", response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}