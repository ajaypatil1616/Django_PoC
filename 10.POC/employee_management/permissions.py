from .models import Admin, Employee
from rest_framework.permissions import BasePermission
from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.exceptions import AuthenticationFailed

#Cheking user is admin or not
class IsAdminOrNot(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'

#Making sure Manager has access to only view and update himself
class HasManagerItselfAccess(BasePermission):
    def has_permission(self, request, view):
        token_passed = request.headers.get("Authorization")

        if not token_passed or not token_passed.startswith('Bearer '):
            return False
        manager_id = AccessToken(token_passed.split()[1]).payload['user_id']
        url_manager_id = view.kwargs.get('pk')
        if url_manager_id == manager_id:
            return True
        return False
    
#Cheking Manager has access or not on specific employee
class HasManagerAccessOrNot(BasePermission):
    def has_object_permission(self, request, view, obj):
        token = request.headers.get('Authorization')
        
        if not token or not token.startswith('Bearer '):
            return False
        try :
            access = token.split()[1]
            manager_id =AccessToken(access).payload['user_id']
            emp_id = view.kwargs.get('pk')
            employee = Employee.objects.get(pk = emp_id)
            if manager_id == employee.manager_id:
                return True
        except :
            return False



#Cheking user is employee or not
class IsValidEmployeeOrNot(BasePermission):
    def has_permission(self, request, view):
        token_passed = request.headers.get("Authorization")
      
        if not token_passed or not token_passed.startswith('Bearer '):
            return False
      
        token = token_passed.split()[1]
        try :
            access_token = AccessToken(token)
            user_id = access_token.payload['user_id']
            emp_id = int(view.kwargs.get('pk'))
            if emp_id == user_id:
                return True
        except:
            return False