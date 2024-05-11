from rest_framework import serializers
from .models import Tenant
import re

class TenantSerilizations(serializers.ModelSerializer):
    age = serializers.IntegerField()
    class Meta:
        model = Tenant
        # fields = ['name','age','email','number','payment','is_active']
        exclude = ['joined']
    
    def create(self, validated_data):
        return Tenant.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)
        instance.number = validated_data.get('number', instance.number)
        instance.payment = validated_data.get('payment',instance.payment)
        instance.is_active = validated_data.get('is_active',instance.is_active)
        instance.save()
        return instance
    
    def validate_age(self, value):
            try:
                age = int(value)
                if age > 58 or age <18 :
                    raise serializers.ValidationError("Age must be in range(18,58)")
                return age
            except ValueError:
                raise serializers.ValidationError("AGe must be INT")
            
    def validate(self, data):
        age = data.get('age')
        email = data.get('email')
        number = data.get('number')
        
        # if age and (age <18 or age >58):
        #     raise serializers.ValidationError("Age must be in range (18,58)")
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',email):
            raise serializers.ValidationError("Enter correct Email id")
        elif len(number) <10 or len(number)> 10:
            raise serializers.ValidationError("Enter 10 digits number only")
        else:
            return data
        
        
                    