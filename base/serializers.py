from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     user  = User.objects.create_user(**validated_data) 
        # return user      
    def create(self, validated_data): 
            user = User(
                email=validated_data['email'],
                password=validated_data.get('password', ''),  
                role=validated_data.get('role', 'regular_user')
        )
            user.set_password(validated_data['password'])  # Hash password
            user.save()
            return user
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class User_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Profile
        fields = '__all__'  

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'  

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = '__all__'

class Audit_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit_Log
        fields = '__all__'  

class Backup_FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backup_File
        fields = '__all__'

class Recovery_FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recovery_File
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'  