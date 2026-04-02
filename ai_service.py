import os
import json
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

MODEL = "meta-llama/Llama-3.3-70B-Instruct"

SYSTEM_PROMPT = """
You are an expert ATS (Applicant Tracking System) resume analyzer.
Analyze the given resume against the job description for the specific company and role.
You MUST return ONLY valid JSON. No extra text, no markdown, no explanation.

Return exactly this JSON structure:
{
  "ats_score": <integer 0-100>,
  "keyword_match": <integer 0-100>,
  "format_score": <integer 0-100>,
  "experience_match": <integer 0-100>,
  "missing_keywords": ["keyword1", "keyword2"],
  "matched_keywords": ["keyword1", "keyword2"],
  "suggestions": [
    {
      "category": "Keywords",
      "priority": "high",
      "message": "Add these missing skills to your resume"
    }
  ],
  "summary": "2-3 sentence overall summary of the resume fit"
}

Priority must be: "high", "medium", or "low"
Be company-specific. If the company is Google, mention data structures.
If it is a startup, mention ownership and versatility.
"""

def analyze_resume(
    resume_text: str,
    job_description: str,
    company_name: str,
    role: str
) -> dict:

    user_message = f"""
Company applying to: {company_name}
Role: {role}

--- JOB DESCRIPTION ---
{job_description}

--- RESUME TEXT ---
{resume_text}

Analyze this resume for ATS compatibility and return JSON only.
"""

    client = InferenceClient(api_key=HF_TOKEN)

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": user_message}
        ],
        max_tokens=1500,
        temperature=0.3
    )

    raw_content = response.choices[0].message.content

    cleaned = raw_content.strip()
    cleaned = cleaned.removeprefix("```json")
    cleaned = cleaned.removeprefix("```")
    cleaned = cleaned.removesuffix("```")
    cleaned = cleaned.strip()

    return json.loads(cleaned)
