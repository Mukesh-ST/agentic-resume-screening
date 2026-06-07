EXTRACT_CANDIDATE_DETAILS = """
You are an expert in resume screening. Your task is to extract relevant details from a resume.
You will receive a resume in text format, and you need to identify key information such as:
- name (string)
- email (string)
- phone (string)
- education (string or null)
- work_experience (integer or null)
- skills (list of strings)
- certifications (list of strings)

Your response must be a valid JSON object.
Use `null` if a value is missing.

Here is the resume text:
{resume_text}

Expected response format:
{{
  "name": "John Doe",
  "email": "abc@gmail.com",
  "phone": "1234567890",
  "education": "Bachelor of Science in Computer Science",
  "work_experience": 7,
  "skills": ["Python", "FastAPI", "Machine Learning"],
  "certifications": ["Certified Python Developer"]
}}
"""
EXTRACT_JD_DETAILS = """
You are an expert in analyzing job descriptions. Extract the following details:
- job_title (string)
- required_skills (list of strings)
- experience_required (integer or null)
- education (string or null)
- responsibilities (list of strings)

Your response must be a valid JSON object.
Use `null` if a value is missing.

Here is the job description:
{jd_text}

Expected response format:
{{
  "job_title": "Software Engineer",
  "required_skills": ["Python", "FastAPI"],
  "experience_required": 3,
  "education": "Bachelor's degree",
  "responsibilities": ["Build APIs", "Write tests"]
}}
"""
CANDIDATE_EVALUATION = """
You are an expert recruiter. Compare the candidate's resume with the job description and evaluate:
- is_suitable (boolean)
- match_score (integer 0-100)
- matching_skills (list of strings)
- missing_skills (list of strings)
- candidate_status (string: "Selected" or "Rejected")
- remarks (string)

Resume Details:
{resume_json}

Job Description:
{jd_json}

Your response must be a valid JSON object.
Expected response format:
{{
  "is_suitable": true,
  "match_score": 85,
  "matching_skills": ["Python", "FastAPI"],
  "missing_skills": ["Docker"],
  "candidate_status": "Selected",
  "remarks": "Strong candidate with relevant experience"
}}
"""