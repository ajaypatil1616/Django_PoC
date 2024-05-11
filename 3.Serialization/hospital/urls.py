# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor-list'),
    path('patients/', views.patient_list, name= 'patient-list'),
]
   
