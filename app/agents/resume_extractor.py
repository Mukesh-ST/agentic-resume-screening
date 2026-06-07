import os
from groq import Groq
from dotenv import load_dotenv
from app.prompts import EXTRACT_CANDIDATE_DETAILS as RESUME_EXTRACTION_PROMPT

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_resume_data(resume_data):
    prompt = RESUME_EXTRACTION_PROMPT.format(resume_text=resume_data)
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    print("Response from Groq:", response.choices[0].message.content)
    return response.choices[0].message.content

def extract_resume_from_pdf(pdf_path):
    import PyPDF2
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return extract_resume_data(text)