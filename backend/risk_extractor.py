import requests


def extract_risks(text):

    prompt = f"""
You are a medical risk extraction assistant.

Extract all risks, complications, side effects, and warnings mentioned in the consent form.

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
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


def extract_summary_risks(summary):

    prompt = f"""
You are a medical risk extraction assistant.

Extract all risks mentioned in the summary.

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
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]