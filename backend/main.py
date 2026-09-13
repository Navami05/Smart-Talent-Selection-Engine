from fastapi import FastAPI, UploadFile, File
import pymupdf
from docx import Document
import io
from utils.text_cleaner import clean_text
from services.jd_extractor import extract_job_description

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Smart Talent Selection Engine API is running"
    }


@app.post("/upload-jd")
async def upload_job_description(file: UploadFile = File(...)):

    allowed_types = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ]

    if file.content_type not in allowed_types:
        return {
            "error": "Only PDF and DOCX files are allowed"
        }

    file_content = await file.read()

    if file.content_type == "application/pdf":

        pdf = pymupdf.open(
            stream=file_content,
            filetype="pdf"
        )

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()

    else:

        document = Document(
            io.BytesIO(file_content)
        )

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"


    text = clean_text(text)

    job_description = extract_job_description(text)

    return {
        "message": "Job description processed successfully",
        "filename": file.filename,
        "data": job_description.model_dump()
    }