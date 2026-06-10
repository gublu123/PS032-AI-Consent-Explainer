from fastapi import FastAPI
from summarizer import simplify_consent_form

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI Consent Form Explainer API Running"
    }

@app.post("/summarize")
def summarize():

    sample_text = """
Procedure:
Appendectomy

Benefits:
Relief from appendicitis.

Risks:
- Infection
- Bleeding
- Adverse reaction to anesthesia
- Blood clots
- Injury to nearby organs
"""

    summary = simplify_consent_form(sample_text)

    return {
        "summary": summary
    }