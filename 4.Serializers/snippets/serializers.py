from rest_framework import serializers
from .models import Snippet

class SnippetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields  = '__all__'
    #Create and return a new `Snippet` instance, given the validated data.
    # def create(self, validated_data):
    #     return Snippet.objects.create(**validated_data)


    # # Update and return an existing `Snippet` instance, given the validated data.
    # def update(self, instance, validated_data):
        
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance