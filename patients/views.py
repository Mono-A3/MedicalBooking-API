from .serializers import PatientSerializer
from .models import Patient

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class ListPatientView(ListAPIView, CreateAPIView):
    allowed_methods = ["GET", "POST"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DetailPatientsView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ["GET", "PUT", "DELETE"]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    lookup_field = "pk"
