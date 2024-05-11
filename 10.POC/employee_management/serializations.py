from rest_framework import serializers
from .models import Admin,  Employee
import re

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['username','email','password', 'role']
        extra_kwargs = {'password' :{'write_only':True}}
        
        
    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')          
            
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',email):
            raise serializers.ValidationError("Enter correct email ")
        elif(len(password.strip()) == 0 or len(password.strip()) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password)):
            raise serializers.ValidationError("Passowod must Contain a uppercase, lowecase, digit and minimum len of 8 ")
        elif(len(username.strip()) == 0 or  not any(char.islower() for char in username) or not any(char.isdigit() for char in username)):
            raise serializers.ValidationError("username must Contain a lowecase and digit ")
             
        else:
            return data
        
    
class EmployeeSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Employee
        fields = '__all__'
       
    def create(self, validated_data):
       manager =  self.context['request'].user
       validated_data['manager'] =manager
       return super().create(validated_data)
   
    def validate(self, data):
        name = data.get('name')
        age = data.get('age')   
        password = data.get('password')       
        username = data.get('username')       
          
            
        if(len(name.strip()) == 0 or  any(char.isdigit() for char in name)):
            raise serializers.ValidationError("Name cannot be empty Or can not contains digits")
        elif(age < 18 or age > 58):
            raise serializers.ValidationError("Age must be in range(18,58)")
        elif(not password or len(password.strip()) < 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password)):
            raise serializers.ValidationError("Passowod must Contain a uppercase, lowecase, digit and minimum len of 8 ")
        elif(len(username.strip()) == 0 or  not any(char.islower() for char in username) or not any(char.isdigit() for char in username)):
            raise serializers.ValidationError("username must Contain a lowecase and digit ")
            
        else:
            return data
       

    