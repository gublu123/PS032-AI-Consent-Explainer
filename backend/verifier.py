import re

def verify_risks(original_risks, summary_risks):

    missing = []

    original_lines = original_risks.split("\n")

    summary_text = summary_risks.lower()

    for risk in original_lines:

        risk = risk.strip()

        if not risk:
            continue

        # Remove bullets, numbering and markdown
        risk = re.sub(r"^[\-\*\•\d\.\)\s]+", "", risk)

        risk = risk.replace("**", "").strip()

        if len(risk) < 3:
            continue

        if risk.lower() not in summary_text:
            missing.append(risk)

    return missing