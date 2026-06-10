from fastapi import FastAPI, UploadFile, File
from pdf_parser import extract_text
from summarizer import simplify_consent_form
from risk_extractor import extract_risks, extract_summary_risks
from verifier import verify_risks
import os

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI Consent Form Explainer API Running"
    }

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        buffer.write(await file.read())

    text = extract_text(temp_path)

    summary = simplify_consent_form(text)

    risks = extract_risks(text)

    summary_risks = extract_summary_risks(summary)

    missing = verify_risks(risks, summary_risks)

    os.remove(temp_path)

    return {
        "summary": summary,
        "risks": risks,
        "missing_risks": missing
    }