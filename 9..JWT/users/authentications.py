from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User
import jwt


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        
        token = request.headers.get('Authorization')
        if not token :
            raise AuthenticationFailed("Token not Found")
        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
            user_id = payload.get('id')
            user = User.objects.filter(id = user_id).first()
            if not user :
                raise AuthenticationFailed("user  not found")
            return(user, token)
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid Token")
        except User.DoesNotExist:
            raise AuthenticationFailed("User not Found")
        
        
        