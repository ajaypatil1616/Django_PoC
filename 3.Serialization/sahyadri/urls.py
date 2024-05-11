from django.urls import path
from .views import ManagerListCreateAPIView, EmployeeListCreateAPIView,ManagerRetrieveUpdateDestroy,EmployeeRetrieveUpdateDestroy

urlpatterns = [
    path('managers/', ManagerListCreateAPIView.as_view()),
    path('managers/<int:pk>/', ManagerRetrieveUpdateDestroy.as_view()),
    path('employees/', EmployeeListCreateAPIView.as_view()),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroy.as_view()),
    
]