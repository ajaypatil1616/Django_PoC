from .models import Admin, Employee
from rest_framework.authentication import BaseAuthentication
import jwt
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate

#Authenticating Employee
class IsEmployeeOrNot(BaseAuthentication):
    def authenticate(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if username is None or password is None:
            return None
        
        try:
            employee = Employee.objects.get(username = username ,password = password)
            if employee:
                return (employee, None)
        except :
            return None
        raise AuthenticationFailed("Invalid username or password")
