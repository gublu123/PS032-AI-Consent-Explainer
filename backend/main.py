from pdf_parser import extract_text

pdf_path = "../sample_pdfs/surgery_consent.pdf"

text = extract_text(pdf_path)

print("----- EXTRACTED TEXT -----")
print(text)