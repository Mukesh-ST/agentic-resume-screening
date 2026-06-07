Agentic Resume Screening

AI-powered resume screening application that automatically extracts candidate information from resumes and matches it against job descriptions using Large Language Models.

Overview
Upload a resume PDF, the AI extracts structured candidate data, matches it with the job description, and displays a complete candidate evaluation through a clean web interface.

Tech Stack
FastAPI is used for the REST API backend that handles resume processing requests.
Streamlit powers the frontend web interface where users upload resumes and view results.
Groq AI with Llama 3.3 70B model acts as the language model for intelligent resume and JD analysis.
PyPDF2 handles PDF text extraction from both resume and job description files.
Python 3.11 is the core programming language used throughout the project.
python-dotenv manages environment variables and API key configuration securely.

Project Structure
agentic_resume_screening/
├── app/
│   ├── agents/
│   │   ├── resume_extractor.py
│   │   ├── jd_extractor.py
│   │   └── candidate_evaluation.py
│   ├── resources/
│   ├── ui/
│   │   └── streamlit.py
│   ├── main.py
│   ├── parsepdf.py
│   └── prompts.py
├── .env.example
├── requirements.txt
└── README.md

Getting Started

Step 1 - Clone the repository
git clone https://github.com/Mukesh-ST/agentic-resume-screening.git
cd agentic-resume-screening

Step 2 - Create virtual environment
python -m venv .venv
.venv\Scripts\activate

Step 3 - Install all dependencies
pip install -r requirements.txt

Step 4 - Configure environment variables
Create a .env file in the root folder and add your Groq API key as shown below.
GROQ_API_KEY=your_key_here
Get your completely free API key at https://console.groq.com

Step 5 - Add your job description
Place your job description PDF file inside the app/resources/ folder.

Running the Application
You need two terminals running simultaneously for the app to work properly.

Terminal 1 runs the FastAPI backend server:
uvicorn app.main:app --reload --port 8000

Terminal 2 runs the Streamlit frontend:
streamlit run app/ui/streamlit.py

Once both are running, open your browser and go to http://localhost:8501

How It Works
The user uploads a resume PDF through the Streamlit web interface.
PyPDF2 extracts the raw text content from the uploaded PDF file.
The extracted text is sent to the FastAPI backend via a POST request.
Groq AI with Llama 3.3 70B analyzes the resume and returns structured JSON data containing name, email, phone, education, work experience, skills and certifications.
The job description PDF stored in the resources folder is also extracted and analyzed by the AI.
The candidate evaluation agent compares the resume data against the job description and determines candidate suitability.
The final structured results are displayed on the Streamlit UI in a clean minimal format.

Requirements
Python 3.11 or higher must be installed on your system.
A free Groq API key is required which can be obtained at console.groq.com with no credit card needed.

Dependencies
fastapi
uvicorn
streamlit
groq
PyPDF2
python-dotenv
python-multipart
requests


Built using Groq AI, FastAPI and Streamlit
