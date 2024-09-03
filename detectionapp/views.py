from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
import uuid
from .features import detect_currency, read_text, identify_objects, describe_spatial, recognize_face

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def upload_or_stream(request):
    feature = request.GET.get('feature', 'currency_detection')

    if request.method == 'POST':
        feature = request.POST.get('feature', feature)

        if 'image' in request.FILES:
            image = request.FILES.get('image')

            extension = os.path.splitext(image.name)[1]
            random_filename = f"{uuid.uuid4()}{extension}"
            image_path = os.path.join(settings.MEDIA_ROOT, 'images', random_filename)

            os.makedirs(os.path.dirname(image_path), exist_ok=True)

            try:
                with open(image_path, 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)

            print(f"Saved image to {image_path}")

            try:
                if feature == 'currency_detection':
                    result, result_filename = detect_currency(image_path)
                elif feature == 'text_reading':
                    result = read_text(image_path)
                    result_filename = None
                elif feature == 'object_identification':
                    result = identify_objects(image_path)
                    result_filename = None
                elif feature == 'spatial_description':
                    result = describe_spatial(image_path)
                    result_filename = None
                elif feature == 'facial_recognition':
                    result, result_filename = recognize_face(image_path)
                else:
                    result = "Invalid feature specified"
                    result_filename = None
            except Exception as e:
                result = f"An error occurred: {str(e)}"
                result_filename = None

            print(f"Feature result: {result}")

            # Redirect to result view with result and filename as query parameters
            return HttpResponseRedirect(f"{reverse('result_view')}?result={result}&image_url=/media/{result_filename if result_filename else ''}")
        else:
            return JsonResponse({'error': 'No image file provided'}, status=400)

    return render(request, 'upload_or_stream.html', {'feature': feature})

def result_view(request):
    result = request.GET.get('result', 'No result available')
    image_url = request.GET.get('image_url', '')  # Get the image URL from query parameters if available

    return render(request, 'result.html', {'result': result, 'image_url': image_url})