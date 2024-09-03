import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update path as needed

def detect_currency(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return "Image not found or cannot be read"
    # Add debug print
    print(f"Detecting currency for {image_path}")
    
def read_text(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return "Image not found or cannot be read"
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    try:
        text = pytesseract.image_to_string(gray)
    except pytesseract.TesseractNotFoundError:
        return "Tesseract executable not found"
    
    if text.strip():
        return f"Detected Text: {text.strip()}"
    else:
        return "No text detected"

def identify_objects(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return "Image not found or cannot be read"
    # Add debug print
    print(f"Identifying objects for {image_path}")
    return "Objects Identified (Dummy Result)"

def describe_spatial(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return "Image not found or cannot be read"
    # Add debug print
    print(f"Describing spatial for {image_path}")
    return "Spatial Description (Dummy Result)"

def recognize_face(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return "Image not found or cannot be read"
    # Add debug print
    print(f"Recognizing face for {image_path}")
    return "Face Recognized (Dummy Result)"
