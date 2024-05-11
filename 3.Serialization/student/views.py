from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Student
from .serializer import CourseSerializer,StudentSerializer

class CourceListCreateAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many =True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSerializer(data = request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)

class StudentListCreateAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)

    def post(self,request):
        serialize = StudentSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status= 201)
        return Response(serialize.errors, status= 400)



