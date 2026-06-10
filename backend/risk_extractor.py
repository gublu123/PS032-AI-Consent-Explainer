import requests

def extract_risks(text):

    prompt = f"""
You are a medical risk extraction assistant.

Extract all risks, complications, side effects, and warnings mentioned in the consent form.

Return only a bullet list.

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