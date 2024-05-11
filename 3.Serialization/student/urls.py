from django.urls import path
from .views import  StudentListCreateAPIView, CourceListCreateAPIView

urlpatterns = [
    path('student/', StudentListCreateAPIView.as_view(), name = 'student'),
    path('course/', CourceListCreateAPIView.as_view(), name = 'course')
]