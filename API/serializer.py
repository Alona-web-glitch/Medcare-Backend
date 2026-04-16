from rest_framework import serializers
from Doctor.models import *
from Appointment.models import *
from django.contrib.auth.models import User


# DOCTOR
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'

# APPOINTMENT
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

#REGISTER
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']


    def create(self, validated_data):
        user = User.objects.create_user(
        username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password']
    )
        return user

# USER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
