import requests

def simplify_consent_form(text):

    prompt = f"""
You are a healthcare communication assistant.

Your task is to explain a medical consent form in simple language.

Rules:
1. Do not change the legal meaning.
2. Do not remove any risks.
3. Explain medical terms in plain English.
4. Create sections:
   - Procedure
   - Benefits
   - Risks
   - Recovery
5. If information is missing, say "Not specified".

Consent Form:

{text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]