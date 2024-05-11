from django.urls import path
from .views import AdminCreateAPI,AdminLogInAPI,ListAllManagerAndEmployees,ManagerCreateAPI
from .views import ManagerLogIn,ManagerRetrieveUpdateDestroy,RetrieveUpdateManager
from .views import EmployeeRegistration,EmployeeList,EmployeeRetrieveUpdateDestroy,EmployeeLogin,EmployeeRetrieveUpdate

urlpatterns = [
    #Admin 
    path('register-admin/',AdminCreateAPI.as_view(), name='admin_register'),
    path('login-admin/',AdminLogInAPI.as_view(), name='admin_login'),      
    path('admin-dash/',ListAllManagerAndEmployees.as_view(), name='admin_dashboard'),
    
    #Manager
    path('register-manager/',ManagerCreateAPI.as_view(), name='manager_register'),
    path('login-manager/',ManagerLogIn.as_view(), name='manager_login'),
    path('manager/<int:pk>/',ManagerRetrieveUpdateDestroy.as_view(), name='manager_RUD'),
    path('manager-RD/<int:pk>/',RetrieveUpdateManager.as_view(), name='manager_RU'),
    
    # Employee
    path('register-emp/',EmployeeRegistration.as_view(), name='emp_register'),
    path('emp-list/',EmployeeList.as_view(), name='emp_list'),
    path('emp/<int:pk>/',EmployeeRetrieveUpdateDestroy.as_view(), name='emp_RUD'), 
    path('emp-login/',EmployeeLogin.as_view(), name='emp_login'), 
    path('emp-RU/<int:pk>/',EmployeeRetrieveUpdate.as_view(), name='emp_RU'), 
]