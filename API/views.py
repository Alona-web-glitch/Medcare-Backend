from django.shortcuts import render
from .serializer import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


# Create your views here.

# DOCTOR
class DoctorView(generics.ListCreateAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [AllowAny]

class DoctorViewDetails(generics.RetrieveDestroyAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [AllowAny]

# APPOINTMENT
class AppointmentView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]

class AppointmentViewDetails(generics.RetrieveDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]

#REGISTER
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created"}, status=201)

        print(serializer.errors)  
        return Response(serializer.errors, status=400)
# USER
class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]