# Generated by Django 4.2.7 on 2023-11-18 12:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('PatientID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('DateOfBirth', models.DateField()),
                ('AppointmentDate', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('ContactInformation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('PrescriptionID', models.AutoField(primary_key=True, serialize=False)),
                ('Medications', models.CharField(max_length=255)),
                ('Dosages', models.CharField(max_length=100)),
                ('Instructions', models.TextField()),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
                ('PrescribedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalReport',
            fields=[
                ('ReportID', models.AutoField(primary_key=True, serialize=False)),
                ('TestResults', models.TextField()),
                ('Diagnoses', models.TextField()),
                ('Date', models.DateField(default=datetime.date.today)),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('HistoryID', models.AutoField(primary_key=True, serialize=False)),
                ('Allergies', models.TextField(blank=True)),
                ('Medications', models.TextField(blank=True)),
                ('PreviousIllnesses', models.TextField(blank=True)),
                ('Surgeries', models.TextField(blank=True)),
                ('PatientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
    ]
