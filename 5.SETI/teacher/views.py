from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .models import Teacher, Student
from .serializers import StudentSerializer, TeacherSerializer, UserSerializer, User
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
        
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                
                'payload': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
              
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Teacher CREATE and LIST
class TeacherCRAPI(APIView):
   
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format =None):
        teachers = Teacher.objects.all()
        serilizer = TeacherSerializer(teachers, many = True)
        return Response(serilizer.data)
    
    def post(self, request, format = None):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= 201)
        return Response(serializer.errors, status= 400)

#Teacher Retrieve Update and Destroy
class TeacherRUDAPI(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk = pk)
        except Teacher.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        teacher = self. get_object(pk)
        serialize  = TeacherSerializer(teacher)
        return Response(serialize.data)
    
    def put(self, request, pk):
        teacher = self.get_object(pk)
        serialize =TeacherSerializer(teacher, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status= 400)
    
    def delete(self, request, pk):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status= 204)

#Student Create and List
class StudentCRAPI(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format =None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)
    
    def post(self, request, format =None):
        serialize = StudentSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status= 200)
        return Response(serialize.errors, status= 400)


class StudentRUDAPI(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
   
    
    def get_object(self, pk):
        try :
            return Student.objects.get(pk = pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        student = self.get_object(pk)
        serialize = StudentSerializer(student)
        return Response(serialize.data)
    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)



