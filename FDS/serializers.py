from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['email', 'password','role']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data): 
            user = User(
                email=validated_data['email'],
                password=validated_data.get('password', ''),  
                role=validated_data.get('role', 'standard_user')
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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:            
        model = File
        fields = '__all__'

class Audit_LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit_Log
        fields = '__all__'

class Access_RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access_Request
        fields = '__all__'

class File_BackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = File_Backup
        fields = '__all__'

class File_RecoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = File_Recovery
        fields = '__all__'

# class WorkflowSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Workflow
#         fields = '__all__'

# class Workflow_ResponsibilitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Workflow_Responsibility
#         fields = '__all__'

class Notification_TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification_Token
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
