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

Consent Form:

{text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": 2048
            }
        }
    )

    print("\n========== RAW RESPONSE ==========")
    print(response.status_code)
    print(response.text)
    print("==================================\n")

    if response.status_code != 200:
        raise Exception(
            f"Ollama Error ({response.status_code}): {response.text}"
        )

    data = response.json()

    answer = (
        data.get("response", "").strip()
        or data.get("thinking", "").strip()
    )

    return answer