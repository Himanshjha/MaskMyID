import re
import spacy

# Use small spaCy model which is lightweight and easier to load
nlp = spacy.load("en_core_web_sm")

def detect_pii(ocr_results):
    pii_boxes = []

    keywords = [
        "head of family", "member name", "address", "mobile number",
        "relation", "ration card number", "guardian name", "date of issue",
        "permanent address", "id no", "voter id", "driving license",
        "passport no", "passport number", "pan number", "pan no"
    ]

    for (bbox, text, _) in ocr_results:
        clean_text = text.strip()

        if re.search(r"\b\d{4}\s\d{4}\s\d{4}\b|\bX{3,4}-X{3,4}-\d{4}\b", clean_text):
            pii_boxes.append(bbox)
        elif re.search(r"\b(?:\+91[-\s]?|0)?[6-9]\d{9}\b", clean_text):
            pii_boxes.append(bbox)
        elif re.search(r"\b\d{18}\b", clean_text):
            pii_boxes.append(bbox)
        elif re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", clean_text):
            pii_boxes.append(bbox)
        elif (re.search(r"\b\d{2}[-/]\d{2}[-/]\d{4}\b|\b\d{4}[-/]\d{2}[-/]\d{2}\b", clean_text)
              or re.search(r"\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{4}\b", clean_text, re.IGNORECASE)):
            pii_boxes.append(bbox)
        elif re.search(r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b", clean_text, re.IGNORECASE):
            pii_boxes.append(bbox)
        elif re.search(r"\b[A-Z]\d{7}\b", clean_text, re.IGNORECASE):
            pii_boxes.append(bbox)
        elif re.search(r"\b[A-Z]{2}\d{11}\b", clean_text, re.IGNORECASE):
            pii_boxes.append(bbox)
        elif any(key in clean_text.lower() for key in keywords):
            pii_boxes.append(bbox)
        else:
            doc = nlp(clean_text)
            for ent in doc.ents:
                if ent.label_ == "PERSON" and 2 <= len(clean_text.split()) <= 4:
                    pii_boxes.append(bbox)
                elif ent.label_ in ["GPE", "LOC", "ORG"]:
                    pii_boxes.append(bbox)
    return pii_boxes
