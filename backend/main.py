from summarizer import simplify_consent_form
from risk_extractor import extract_risks, extract_summary_risks
from verifier import verify_risks

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

# Generate summary
summary = simplify_consent_form(text)

# Extract risks from original text
risks = extract_risks(text)

# Extract risks from generated summary
summary_risks = extract_summary_risks(summary)

# Verify risks
missing = verify_risks(risks, summary_risks)

print("\n===== PATIENT FRIENDLY SUMMARY =====\n")
print(summary)

print("\n===== DETECTED RISKS =====\n")
print(risks)

print("\n===== RISKS FOUND IN SUMMARY =====\n")
print(summary_risks)

print("\n===== VERIFICATION RESULT =====\n")

if missing:
    print("WARNING: Missing Risks")
    for risk in missing:
        print(risk)
else:
    print("All risks preserved")