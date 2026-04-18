from django.urls import path
from .views import *

urlpatterns = [
    path('doctor/', DoctorView.as_view(), name='doctor'),
    path('doctor/<int:pk>/', DoctorViewDetails.as_view(), name='doctordetails'),

    path('booking/', AppointmentView.as_view(), name='appointment'),
    path('booking/<int:pk>/', AppointmentViewDetails.as_view(), name='appointmentdetails'),

    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserView.as_view(), name='user'),
]