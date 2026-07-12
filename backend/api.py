from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from pdf_parser import extract_text
from summarizer import simplify_consent_form
from risk_extractor import extract_risks, extract_summary_risks
from verifier import verify_risks

import requests
import os
import time

from typing import List

app = FastAPI()

# =====================================================
# CORS
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================================
# Home
# =====================================================

@app.get("/")
def home():

    return {

        "message": "AI Consent Form Explainer API Running"

    }


# =====================================================
# Get Installed Ollama Models
# =====================================================

@app.get("/models")
def get_models():

    try:

        response = requests.get(
            "http://localhost:11434/api/tags"
        )

        if response.status_code != 200:

            return {

                "models": [],

                "error": "Unable to fetch models from Ollama"

            }

        data = response.json()

        models = []

        for model in data.get("models", []):

            if model["name"].startswith("qwen3.5"):
                continue

            models.append(model["name"])

        return {

            "models": models

        }

    except Exception as e:

        return {

            "models": [],

            "error": str(e)

        }


# =====================================================
# Upload PDF / TXT
# =====================================================

@app.post("/upload-pdf")
async def upload_pdf(

    file: UploadFile = File(...),

    model: str = Form(...)

):

    print(f"Selected Model : {model}")

    temp_path = f"temp_{file.filename}"

    try:

        with open(temp_path, "wb") as buffer:

            buffer.write(await file.read())

        # ---------------------------------------

        # Read Uploaded File

        # ---------------------------------------

        if file.filename.lower().endswith(".pdf"):

            text = extract_text(temp_path)

        elif file.filename.lower().endswith(".txt"):

            with open(

                temp_path,

                "r",

                encoding="utf-8"

            ) as f:

                text = f.read()

        else:

            return {

                "error":

                "Only PDF and TXT files are supported."

            }

        if not text.strip():

            return {

                "error":

                "No readable text found."

            }

        # ---------------------------------------

        # AI Processing

        # ---------------------------------------

        start = time.time()

        summary = simplify_consent_form(

            text,

            model

        )

        risks = extract_risks(

            text,

            model

        )

        summary_risks = extract_summary_risks(

            summary,

            model

        )

        missing = verify_risks(

            risks,

            summary_risks

        )

        elapsed = round(

            time.time() - start,

            2

        )

        return {

            "model_used": model,

            "processing_time": elapsed,

            "summary": summary,

            "risks": risks,

            "missing_risks": missing

        }

    except Exception as e:

        print("Backend Error:", e)

        return {

            "error": str(e)

        }

    finally:

        if os.path.exists(temp_path):

            os.remove(temp_path)


# =====================================================
# Compare Multiple Models
# =====================================================

@app.post("/compare-models")
async def compare_models(
    file: UploadFile = File(...),
    models: List[str] = Form(...)
):

    print("Selected Models:", models)

    temp_path = f"temp_{file.filename}"

    try:

        with open(temp_path, "wb") as buffer:
            buffer.write(await file.read())

        # --------------------
        # Read File
        # --------------------

        if file.filename.lower().endswith(".pdf"):

            text = extract_text(temp_path)

        elif file.filename.lower().endswith(".txt"):

            with open(temp_path, "r", encoding="utf-8") as f:
                text = f.read()

        else:

            return {
                "error": "Only PDF and TXT files are supported."
            }

        if not text.strip():

            return {
                "error": "No readable text found."
            }

        # --------------------
        # Run Comparison
        # --------------------

        results = []

        for model in models:

            print(f"\nRunning Model: {model}")

            start = time.time()

            try:

                summary = simplify_consent_form(
                    text,
                    model
                )

                risks = extract_risks(
                    text,
                    model
                )

                summary_risks = extract_summary_risks(
                    summary,
                    model
                )

                missing = verify_risks(
                    risks,
                    summary_risks
                )

                elapsed = round(
                    time.time() - start,
                    2
                )

                results.append({

                    "model": model,

                    "time": elapsed,

                    "summary": summary,

                    "risks": risks,

                    "missing_risks": missing

                })

            except Exception as e:

                print(f"Error while running {model}: {e}")

                results.append({

                    "model": model,

                    "time": 0,

                    "summary": "Generation Failed",

                    "risks": "Generation Failed",

                    "missing_risks": [],

                    "error": str(e)

                })

        return {

            "results": results

        }

    except Exception as e:

        print("Compare Models Error:", e)

        return {

            "error": str(e)

        }

    finally:

        if os.path.exists(temp_path):

            os.remove(temp_path)