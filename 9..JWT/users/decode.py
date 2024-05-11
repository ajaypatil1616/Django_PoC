from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
class decode(request):
    token = request.headers.get('Authorization')
       
        if not token :
            raise AuthenticationFailed("Token not FOund")
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload.get('id')
            if not user_id:
                raise AuthenticationFailed("User ID not Found")
            user = User.objects.filter(id = user_id).first()
            if not user :
                raise AuthenticationFailed("User not Found")
            serializer = UserSerializer(user)
            return Response(serializer.data)
            
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError as e:
            raise AuthenticationFailed("Invalid token") from e
       