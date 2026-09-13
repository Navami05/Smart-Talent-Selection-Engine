import os
import json
from dotenv import load_dotenv
from google import genai

from models.job import JobDescription

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def extract_job_description(text: str) -> JobDescription:
    prompt = f"""
You are a job description information extraction system.

Extract structured information from the job description below.

Return ONLY valid JSON with these fields:

{{
    "job_title": "",
    "company": "",
    "location": "",
    "department": "",
    "experience": "",
    "skills": [],
    "education": [],
    "responsibilities": [],
    "preferred_skills": []
}}

Rules:
1. Use only information explicitly present in the job description.
2. Do not invent or assume information.
3. If a field is not mentioned, use an empty string or empty list.
4. Keep skills as separate items.
5. Keep responsibilities as separate items.
6. Put optional/preferred skills in "preferred_skills".
7. Return ONLY JSON. Do not include markdown or explanations.

JOB DESCRIPTION:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    result = json.loads(response.text)

    return JobDescription(**result)