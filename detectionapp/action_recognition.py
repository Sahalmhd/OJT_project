import os
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from django.conf import settings

# Set the path to your .keras model file
MODEL_PATH = os.path.join(settings.BASE_DIR, 'models', 'saved_models', 'i3d_keras_model.keras')

# Load the model
model = None  # Initialize globally

try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None  # Ensure model is None if loading fails

# Define your action recognition function
def recognize_action(video_path):
    global model  # Explicitly declare model as global to ensure the correct scope

    if model is None:
        print("Model is not loaded.")
        return "No action recognized"

    cap = cv2.VideoCapture(video_path)
    actions = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Preprocess the frame
        frame = cv2.resize(frame, (224, 224))  # Adjust as needed
        frame = frame / 255.0  # Normalize
        frame = np.expand_dims(frame, axis=0)
        
        # Predict action
        try:
            prediction = model.predict(frame)
            action = np.argmax(prediction)  # Taking the class with the highest probability
            actions.append(action)
        except Exception as e:
            print(f"Error during prediction: {e}")

    cap.release()
    
    # Return the most frequent action
    if actions:
        return max(set(actions), key=actions.count)
    else:
        return "No action recognized"
