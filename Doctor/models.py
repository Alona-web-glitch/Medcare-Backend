from django.db import models

# Create your models here.
class Doctors(models.Model):
    img = models.ImageField(upload_to='media/',null=True, blank=True)
    name = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    about = models.CharField(max_length=500,blank=True, null=True)
    fee = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    gender = models.CharField( max_length=10,choices=GENDER_CHOICES,default='Male')
    def __str__(self):
        return self.name