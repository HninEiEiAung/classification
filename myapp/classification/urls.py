# classification/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("predict/", views.JsonResponse, name="predict"),
]
