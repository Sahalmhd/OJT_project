from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def upload_or_stream(request):
    feature = request.GET.get('feature', 'currency_detection')  # Default to 'currency_detection' if no feature is provided

    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES.get('image')
            image_path = os.path.join(settings.MEDIA_ROOT, 'images', image.name)
            os.makedirs(os.path.dirname(image_path), exist_ok=True)

            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            # Determine result based on the feature
            if feature == 'currency_detection':
                result = detect_currency(image_path)
            elif feature == 'text_reading':
                result = read_text(image_path)
            elif feature == 'object_identification':
                result = identify_objects(image_path)
            elif feature == 'spatial_description':
                result = describe_spatial(image_path)
            elif feature == 'facial_recognition':
                result = recognize_face(image_path)
            else:
                result = "Invalid feature specified"

            return JsonResponse({'result': result})
        else:
            return JsonResponse({'error': 'No image file provided'}, status=400)

    return render(request, 'upload_or_stream.html', {'feature': feature})

# Dummy functions for feature placeholders (replace with actual implementations)
def detect_currency(image_path):
    return "Currency Detected"

def read_text(image_path):
    return "Text Detected"

def identify_objects(image_path):
    return "Objects Identified"

def describe_spatial(image_path):
    return "Spatial Description"

def recognize_face(image_path):
    return "Face Recognized"
