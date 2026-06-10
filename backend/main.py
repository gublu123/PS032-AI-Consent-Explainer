from summarizer import simplify_consent_form
from risk_extractor import extract_risks

text = """
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

summary = simplify_consent_form(text)
risks = extract_risks(text)

print(summary)
print("\nDetected Risks:\n")
print(risks)