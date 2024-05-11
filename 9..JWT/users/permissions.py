from rest_framework.permissions import BasePermission
import jwt
from .models import User
from rest_framework.exceptions import AuthenticationFailed,NotFound

class CustomPermissions(BasePermission):
    def has_permission(self, request, view):
        
        token = request.headers.get('Authorization')
        if not token:
            return False
        
        try :            
            payload = jwt.decode(token, 'secret', algorithms='HS256')
            user_id = payload.get('id')
            user = User.objects.filter(id = user_id).first()
            
            if not user:
                raise NotFound("User not Found")
            
            request.user = user
            return True   
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")
        except jwt.DecodeError:
            raise AuthenticationFailed("Token is invalid")
        
        
        return False
             
    # def has_object_permission(self, request, view, obj):
    #     return super().has_object_permission(request, view, obj)
        
        