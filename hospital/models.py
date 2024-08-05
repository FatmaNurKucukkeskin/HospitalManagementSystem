from django.db import models

# Model for storing information about doctors
class Doctor(models.Model):
    name = models.CharField(max_length=50)  # Name of the doctor
    contact = models.IntegerField(null=True)  # Contact number of the doctor (optional)
    special = models.CharField(max_length=50)  # Specialization of the doctor

    def __str__(self):
        return self.name  # String representation of the doctor object


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    contact = models.IntegerField(null=True)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date1 = models.DateField(null=True)
    time1 = models.TimeField(null=True)

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name