🤖 Agentic Resume Screening App

An AI-powered resume screening application built with Python.

Tech Stack
- FastAPI — Backend API
- Streamlit — Frontend UI
- Groq AI — LLM for analysis
- PyPDF2 — PDF processing

Features
- Upload resume PDF
- AI extracts candidate details
- Matches with job description
- Clean minimal UI

Setup
1. Clone the repo
2. Install requirements: pip install -r requirements.txt
3. Add GROQ_API_KEY in .env file
4. Run backend: uvicorn app.main:app --reload --port 8000
5. Run frontend: streamlit run app/ui/streamlit.py
