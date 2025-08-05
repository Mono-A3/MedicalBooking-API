from django.contrib import admin
from django.urls import path

from .views import ListDoctorView, DetailDoctorsView

urlpatterns = [
    path("doctors/", ListDoctorView.as_view()),
    path("doctors/<int:pk>/", DetailDoctorsView.as_view()),
]
