from django.urls import path
from . import views

urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.getRegisterUser, name='register'),

    path('patients/', views.PatientViewSet.as_view(), name='patients'),
    path('patients_create/', views.CreatePatientView.as_view(), name='create-patient'),
    path('update_patient/<int:PatientID>/', views.UpdatePatientView.as_view(), name='update-patient'),
    path('delete_patient/<int:PatientID>/', views.DeletePatientView.as_view(), name='delete-patient'),

    path('medical_history/<str:pk>/', views.MedicalHistoryListView.as_view(), name='get-medical-history'),
    path('medical_history_create/', views.CreateMedicalHistoryView.as_view(), name='create-medical-history'),
    path('medicalhistoryupdate/<str:HistoryID>/', views.UpdateMedicalHistoryView.as_view(), name='update-medical-history'),
    path('medical_history_delete/<str:HistoryID>/', views.DeleteMedicalHistoryView.as_view(), name='delete-medical-history'),

    path('prescription/<str:pk>/', views.PrescriptionListView.as_view(), name='get-prescription'),
    path('prescription_create/', views.CreatePrescriptionView.as_view(), name='create-prescription'),
    path('prescriptionupdate/<str:PrescriptionID>/', views.UpdatePrescriptionView.as_view(), name='update-prescription'),
    path('prescription_delete/<str:PrescriptionID>/', views.DeletePrescriptionView.as_view(), name='delete-prescription'),
]
