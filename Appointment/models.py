from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=5)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    problem = models.CharField(max_length=200)
    doctor = models.CharField(max_length=100)
    day = models.CharField(max_length=10)
    time = models.CharField(max_length=20)

    def __str__(self):
        return self.name