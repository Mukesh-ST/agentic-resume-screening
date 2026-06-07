from fastapi import FastAPI, UploadFile
from app.parsepdf import parse_pdf
from app.agents.resume_extractor import extract_resume_data
from app.agents.jd_extractor import analyze_jd
from app.agents.candidate_evaluation import evaluate_candidate

app = FastAPI()

@app.post("/screening/")
async def screening(resume: UploadFile):
    resume_text = parse_pdf(resume.file)
    resume_details_extracted = extract_resume_data(resume_text)

    jd_text = ""
    with open("app/resources/Sample JD for Resume Screening.pdf", "rb") as file:
        jd_text = parse_pdf(file)

    jd_extracted = analyze_jd(jd_text)

    evaluation_result = evaluate_candidate(resume_details_extracted, jd_extracted)

    return resume_details_extracted