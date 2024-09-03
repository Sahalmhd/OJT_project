import uuid
import cv2
import numpy as np
import os
from django.conf import settings
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update path as needed

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


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
        return "Image not found or cannot be read", None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Recognizing face for {image_path}")
    print(f"Detected {len(faces)} face(s)")

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    result_filename = f"output_with_faces_{uuid.uuid4()}.jpg"  # Unique filename
    result_image_path = os.path.join(settings.MEDIA_ROOT, result_filename)
    cv2.imwrite(result_image_path, image)

    # Return the relative URL and filename
    return f"Face(s) detected and highlighted. Saved at: /media/{result_filename}", result_filename
