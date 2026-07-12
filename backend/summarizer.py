import requests


def simplify_consent_form(text, model):

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
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        raise Exception(
            f"Ollama Error ({response.status_code}): {response.text}"
        )

    data = response.json()

    if "response" not in data:
        raise Exception(
            f"Invalid Ollama Response: {data}"
        )

    return data["response"]