from services.jd_extractor import extract_job_description


jd_text = """
Assistant Product Manager (APM) – Xpress Health

Location: Kochi
Department: Product & Technology
Company: Xpress Health

We’re looking for an Assistant Product Manager to support the development
and improvement of technology products.

What We're Looking For:
1–3 years of experience in Product Management, Business Analysis,
Project Management or a similar role.

Good understanding of software development and product lifecycle.
Strong communication and stakeholder-management skills.
Strong problem-solving and analytical mindset.

Experience with tools such as Jira, Figma, ClickUp or similar is preferred.
"""


result = extract_job_description(jd_text)

print(result.model_dump_json(indent=2))