from .serializers import DoctorSerializer
from .models import Doctor

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class ListPatientView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailPatientsView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    lookup_field = "pk"
