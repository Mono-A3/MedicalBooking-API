from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from patients.models import Patient
from doctors.models import Doctor


class DoctorViewSetTests(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="Andress",
            last_name="Araquee",
            date_of_birth="2006-02-22",
            contact_number="1234567891",
            email="example@example.com",
            address="hola",
            medical_history="nada",
        )
        self.doctor = Doctor.objects.create(
            first_name="Stiven",
            last_name="Amaya",
            qualification="Profesional",
            contact_number="23123456789",
            email="example@example.com",
            address="Sogayork",
            biography="Sin",
            is_on_vacation=False,
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse("doctor-appointments", kwargs={"pk": self.doctor.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
