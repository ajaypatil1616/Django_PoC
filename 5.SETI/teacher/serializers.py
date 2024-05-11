from rest_framework import serializers
from .models import Teacher, Student
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class StudentSerializer(serializers.Serializer):
    
    name = serializers.CharField(required = True)
    email = serializers.EmailField()
    roll_no = serializers.IntegerField()
    marks = serializers.IntegerField()
    teacher_id = serializers.IntegerField()
    
    def create(self, validated_data):
        teacher_id = validated_data.pop('teacher_id')
        teacher = Teacher.objects.get(pk = teacher_id)        
        student = Student.objects.create(teacher = teacher, **validated_data)
        return student
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.roll_no = validated_data.get('roll_no', instance.roll_no)
        instance.marks = validated_data.get('marks', instance.marks)
        instance.save()
        return instance
    
class TeacherSerializer(serializers.Serializer):
    students = StudentSerializer(many = True, read_only = True)
    
    name = serializers.CharField() 
    email = serializers.EmailField()
    age = serializers.IntegerField()
    number = serializers.CharField()
    subjects = serializers.ChoiceField(choices=(("CNS", "CNS"), ("SE", "SE"), ("AI", "AI")))

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.number = validated_data.get('number', instance.number)
        instance.subjects = validated_data.get('subjects', instance.subjects)
        instance.save()
        return instance