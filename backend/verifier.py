def verify_risks(original_risks, summary_risks):

    missing = []

    original_lines = original_risks.split("\n")

    for risk in original_lines:

        risk = risk.strip()

        # Ignore empty lines
        if not risk:
            continue

        # Only process bullet points
        if not risk.startswith("•"):
            continue

        risk_text = risk.replace("•", "").strip()

        if risk_text.lower() not in summary_risks.lower():
            missing.append(risk_text)

    return missing