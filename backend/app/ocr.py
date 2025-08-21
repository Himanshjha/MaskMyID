import easyocr
from PIL import Image
import cv2

reader = easyocr.Reader(['en', 'hi'])  # Aadhaar ke liye Hindi + English

def extract_text(image_path):
    image = cv2.imread(image_path)
    results = reader.readtext(image)
    # results = [ [bbox, text, confidence], ... ]
    return results, Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
