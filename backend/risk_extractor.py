import requests


def extract_risks(text, model):

    prompt = f"""
You are a medical risk extraction assistant.

Extract ALL risks, complications, side effects, warnings, and possible outcomes mentioned in the consent form.

Rules:
1. Return only bullet points.
2. Do not explain anything.
3. One risk per bullet.

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


def extract_summary_risks(summary, model):

    prompt = f"""
You are a medical risk extraction assistant.

Extract ALL risks mentioned in the patient-friendly summary.

Rules:
1. Return only bullet points.
2. Do not explain anything.
3. One risk per bullet.

Summary:

{summary}
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