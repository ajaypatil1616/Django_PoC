from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .models import Teacher, Student
from .serializers import StudentSerializer, TeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

#Teacher Registration 
class TeacherRegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                
                'payload': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
              
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherTokenGenerationAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            email =serializer.validated_data.get('email')
            teacher = Teacher.objects.get(email = email).first()
            if teacher :
                refresh = RefreshToken.for_user(teacher)
                return Response({
                    'payload':serializer.data,
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                })
        return Response(serializer.errors)
