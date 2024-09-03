# urls.py

from django.urls import path
from .views import home, upload_or_stream, result_view

urlpatterns = [
    path('', home, name='home'),
    path('upload-or-stream/', upload_or_stream, name='upload_or_stream'),
    path('result/', result_view, name='result_view'),
]
