from groq import Groq
from dotenv import load_dotenv
import os
from app.prompts import CANDIDATE_EVALUATION
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def evaluate_candidate(candidate_details: str, jd: str) -> str:
    """
    Function to analyze the extracted text from a resume using Groq's API.
    """
    prompt = CANDIDATE_EVALUATION.format(resume_json=candidate_details, jd_json=jd)
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        print("Response from Groq API:", response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}