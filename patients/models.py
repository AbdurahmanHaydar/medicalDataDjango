from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Patient(models.Model):
    PatientID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    AppointmentDate = models.DateField()
    Gender = models.CharField(max_length=10)
    ContactInformation = models.TextField()

    def __str__(self):
        return self.Name

class MedicalHistory(models.Model):
    HistoryID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Allergies = models.TextField(blank=True)
    Medications = models.TextField(blank=True)
    PreviousIllnesses = models.TextField(blank=True)
    Surgeries = models.TextField(blank=True)

    def __str__(self):
        return f"History of {self.PatientID.Name}"

class Prescription(models.Model):
    PrescriptionID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Medications = models.CharField(max_length=255)
    Dosages = models.CharField(max_length=100)
    Instructions = models.TextField()
    PrescribedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Prescription {self.PrescriptionID} for {self.PatientID.Name}"

class MedicalReport(models.Model):
    ReportID = models.AutoField(primary_key=True)
    PatientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    TestResults = models.TextField()
    Diagnoses = models.TextField()
    Date = models.DateField(default=date.today)

    def __str__(self):
        return f"Report {self.ReportID} for {self.PatientID.Name}"