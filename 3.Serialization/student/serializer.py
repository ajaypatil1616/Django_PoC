from rest_framework import serializers
from .models import Course, Student

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['code']

class StudentSerializer(serializers.ModelSerializer):
    
    courses = CourseSerializer(many =True)
    class Meta:
        model = Student
        fields = '__all__'  
        
    def create(self, validated_data):
        courses_data = validated_data.pop('courses')
        student = Student.objects.create(**validated_data)
        for course_data in courses_data:
            course_code = course_data.get('code')
            course, _ = Course.objects.get_or_create(code=course_code)
            student.courses.add(course)
        return student