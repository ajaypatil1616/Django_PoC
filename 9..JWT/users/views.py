from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from .permissions import CustomPermissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import Http404
from .authentications import CustomAuthentication


#Register API
class Register(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response( serializer.data)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
       
        
        user = User.objects.filter(email = email).first()
        if user is None:
            raise AuthenticationFailed("USER not FOund")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        
        payload = {
            "id":user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes= 5),
            "iat": datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload,'secret', algorithm='HS256')
     
        return Response({"jwt token":token})

#decode token   
class UserView(APIView):
    def get(self, request):
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
        except jwt.InvalidTokenError :
            raise AuthenticationFailed("Invalid token") 

#get all the users
class GetAllUser(APIView):
    
    # permission_classes = [CustomPermissions]
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many = True)
            return Response(serializer.data)            
        except Exception as e:
            return Response(str(e))     

#RUD 
class RetrieveUpdateDelete(APIView):
    permission_classes = [CustomPermissions]

    def get_object(self, pk):
        try:
            return User.objects.get(pk = pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serialize = UserSerializer(user)
        return Response(serialize.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serialize = UserSerializer(user, data= request.data)
        if not serialize.is_valid():
            return Response(serialize.errors)
        serialize.save()
        return Response(serialize.data)
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        if not user:
            return Response("user not found")
        user.delete()
        return Response("user has deleted")
        
 