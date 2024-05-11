from rest_framework import serializers
from .models import Teacher, Student

class StudentSerializer(serializers.Serializer):
    
    name = serializers.CharField()  
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
    students = StudentSerializer(many = True, required = False)
    
    name = serializers.CharField() 
    email = serializers.EmailField()
    password = serializers.CharField()
    age = serializers.IntegerField()
    number = serializers.CharField()
   
    def create(self, validated_data):
       teacher = Teacher.objects.create(email = validated_data['email'], 
                                        age=validated_data['age'],
                                        name = validated_data['name'],
                                        number = validated_data['number'],
                                        password = validated_data['password']) 
       teacher.save()
       return teacher
       
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.number = validated_data.get('number', instance.number)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance