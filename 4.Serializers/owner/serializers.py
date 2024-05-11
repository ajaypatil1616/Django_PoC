from rest_framework import serializers
from .models import Owner, Ten
import re

class OwnerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Owner
        fields = '__all__'
    def validate_age(self, value):
        try:
            age = int(value)
            if(age < 18 or age >58):
                raise serializers.ValidationError("Age must be in range(18,58)")
            return age
        except ValueError:
            raise serializers.ValidationError("Age must be INT")
    def validate(self, data):
        email = data.get('email')
        number = data.get('number')
        t_email = data.get('t_email')
        t_number = data.get('t_number')
        
        if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',email):
            raise serializers.ValidationError("Enter correct email of Owner")
        elif (len(number)< 10 or len(number)>10):
            raise serializers.ValidationError("Number must be 10 digit only")
        else:
            return data
            
        
class TenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ten
        fields = ['t_name','t_age', 't_email', 't_number', 't_rent', 'owner_id']
        
class OwnerTenSerializer(serializers.Serializer):
    owner = OwnerSerializer()
    ten = TenSerializer(many= True)

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        ten_data = validated_data.pop('ten')

        owner_instance = Owner.objects.create(**owner_data)
        ten_instance = Ten.objects.create(owner = owner_instance,**ten_data) # pass instace for foregin key 
        return {'owner': owner_instance, 'ten': ten_instance}
    
    def update(self, instance, validated_data):
        owner_data = validated_data.pop('owner')
        ten_data = validated_data.pop('ten')

        owner_instance = instance.owner
        owner_instance.name = owner_data.get('name',owner_instance.name)
        owner_instance.age = owner_data.get('age',owner_instance.age)
        owner_instance.email = owner_data.get('email',owner_instance.email)
        owner_instance.number = owner_data.get('number',owner_instance.number)
        owner_instance.wing = owner_data.get('wing', owner_instance.wing)
        owner_instance.flat_no = owner_data.get('flat_no',owner_instance.flat_no)
        owner_instance.save()

        ten_instance = instance.ten
        ten_instance.t_name = ten_data.get('t_name',ten_instance.t_name)
        ten_instance.t_age = ten_data.get('t_age',ten_instance.t_age)
        ten_instance.t_email = ten_data.get('t_email',ten_instance.t_email)
        ten_instance.t_number = ten_data.get('t_number',ten_instance.t_number)
        ten_instance.t_rent = ten_data.get('t_rent',ten_instance.t_rent)
        ten_instance.owner = owner_instance # instace passed for foreign key
        ten_instance.save()

        return instance
    
    # def validate_age(self, value):
    #     try:
    #         age = int(value)
    #         if(age < 18 or age >58):
    #             raise serializers.ValidationError("Age must be in range(18,58)")
    #         return age
    #     except ValueError:
    #         raise serializers.ValidationError("Age must be INT")
    # def validate_t_age(self, value):
    #     try:
    #         t_age = int(value)
    #         if(t_age < 18 or t_age > 58):
    #             raise serializers.ValidationError("age must be in range(18,58)")
    #         return t_age
    #     except ValueError:
    #         raise serializers.ValidationError("t_age must be INT")
    # def validate(self, data):
    #     email = data.get('email')
    #     number = data.get('number')
    #     t_email = data.get('t_email')
    #     t_number = data.get('t_number')
        
    #     if not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',email):
    #         raise serializers.ValidationError("Enter correct email of Owner")
    #     elif (len(number)< 10 or len(number)>10):
    #         raise serializers.ValidationError("Number must be 10 digit only")
    #     elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',t_email):
    #         raise serializers.ValidationError("Enter correct email of Owner")
    #     elif (len(t_number)< 10 or len(t_number)>10):
    #         raise serializers.ValidationError("Number must be 10 digit only")
    #     else:
    #         return data
            
        
        