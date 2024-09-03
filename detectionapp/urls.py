from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_or_stream/', views.upload_or_stream, name='upload_or_stream'),
    # other URLs
]
