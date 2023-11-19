from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Patient, MedicalHistory, Prescription
from .serializers import PatientSerializer, MedicalHistorySerializer, MyTokenObtainPairSerializer, PrescriptionSerializer, UserSerializer, UserSerializerWithToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status


class MyTokenObtainPairView(TokenObtainPairView):
    serializer = MyTokenObtainPairSerializer

@api_view(['POST'])
def getRegisterUser(request):
    data = request.data

    try:
        queryset = User.objects.create(
            first_name = data['name'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializerWithToken(queryset, many=False)
        return Response(serializer.data)
    except:
        message = { 'detail': 'User with this email already exists'}
        return Response(message, status = status.HTTP_400_BAD_REQUEST)

class PatientViewSet(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Name', 'Gender', 'AppointmentDate', 'DateOfBirth']

class CreatePatientView(CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class UpdatePatientView(UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'PatientID'

    def get_object(self):
        patient_id = self.kwargs.get('PatientID')
        return Patient.objects.get(PatientID=patient_id)

class DeletePatientView(DestroyAPIView):
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'PatientID'

    def get_object(self):
        patient_id = self.kwargs.get('PatientID')
        return Patient.objects.get(PatientID=patient_id)

# Mediical History
class MedicalHistoryListView(ListAPIView):
    serializer_class = MedicalHistorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["Allergies", "Medications", "PreviousIllnesses", "Surgeries"]

    def get_queryset(self):
        """
        This view should return a list of all the medical history
        for the patient as determined by the pk (PatientID) portion of the URL.
        """
        patient_id = self.kwargs.get('pk')
        return MedicalHistory.objects.filter(PatientID=patient_id)

class CreateMedicalHistoryView(CreateAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Override the perform_create method to handle the creation of
        a new MedicalHistory instance.
        """
        patient_id = self.request.data.get('PatientID')
        patient_instance = Patient.objects.get(PatientID=patient_id)
        serializer.save(PatientID=patient_instance)

class DeleteMedicalHistoryView(DestroyAPIView):
    queryset = MedicalHistory.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'HistoryID'

    def delete(self, request, *args, **kwargs):
        """
        Delete a medical history item and return a custom response message.
        """
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            return Response({'message': 'Medical history item deleted'}, status=response.status_code)
        return response

class UpdateMedicalHistoryView(UpdateAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'HistoryID'

# Prescriptions
class PrescriptionListView(ListAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["Medications", "Dosages", "Instructions"]

    def get_queryset(self):
        """
        This view should return a list of all the medical history
        for the patient as determined by the pk (PatientID) portion of the URL.
        """
        patient_id = self.kwargs.get('pk')
        return Prescription.objects.filter(PatientID=patient_id)

class CreatePrescriptionView(CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Override the perform_create method to handle the creation of
        a new Prescription instance.
        """
        patient_id = self.request.data.get('PatientID')
        patient_instance = Patient.objects.get(PatientID=patient_id)
        serializer.save(PatientID=patient_instance)

class DeletePrescriptionView(DestroyAPIView):
    queryset = Prescription.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'PrescriptionID'

    def delete(self, request, *args, **kwargs):
        """
        Delete a medical history item and return a custom response message.
        """
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            return Response({'message': 'Medical history item deleted'}, status=response.status_code)
        return response

class UpdatePrescriptionView(UpdateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'PrescriptionID'