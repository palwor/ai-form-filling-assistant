import re

def extract_entities(text):
    entities = {}

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # Aadhaar number
    aadhaar = re.search(r"\d{4}\s\d{4}\s\d{4}", text)
    if aadhaar:
        entities["aadhaar"] = aadhaar.group()

    # DOB
    dob_match = re.search(
        r"(DOB|Date of Birth)[:\s]*([\d]{2}/[\d]{2}/[\d]{4})",
        text,
        re.IGNORECASE
    )
    if dob_match:
        entities["dob"] = dob_match.group(2)

    # Name (best guess)
    for line in lines:
        # Skip common non-name lines
        if any(word in line.lower() for word in [
            "government", "india", "male", "female", "dob", "year", "birth"
        ]):
            continue

        # Only alphabets & spaces, 2+ words
        if re.match(r"^[A-Za-z ]{4,}$", line):
            if len(line.split()) >= 2:
                entities["name"] = line
                break

    return entities
