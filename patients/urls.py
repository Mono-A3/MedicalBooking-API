from django.contrib import admin
from django.urls import path

from .views import ListPatientView, DetailPatientsView

urlpatterns = [
    path("patients/", ListPatientView.as_view()),
    path("patients/<int:pk>/", DetailPatientsView.as_view()),
]
