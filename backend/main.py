from pdf_parser import extract_text
from summarizer import simplify_consent_form

pdf_path = "../sample_pdfs/surgery_consent.pdf"

text = extract_text(pdf_path)

summary = simplify_consent_form(text)

print("\n===== PATIENT FRIENDLY SUMMARY =====\n")
print(summary)