from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'role')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'email')

@admin.register(User_Profile)
class User_ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'address', 'number', 'department', 'position', 'image')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  
    list_display = ('name',)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):  
    list_display = ('name', 'type', 'size', 'status', 'description', 'status', 'file_uploaded_date', 'file_uploaded_by',  'category')

@admin.register(Audit_Log)
class Audit_LogAdmin(admin.ModelAdmin):
    list_display = ('user','file', 'action', 'modified_at', 'details')

@admin.register(Access_Request)
class Access_RequestAdmin(admin.ModelAdmin):
    list_display = ('requester', 'file', 'status', 'reason', 'reviewed_by', 'reviewed_at', 'created_at')

@admin.register(File_Backup)
class File_BackupAdmin(admin.ModelAdmin):
    list_display = ('backup_file_name', 'backup_file', 'backup_status', 'backup_type', 'created_at', 'backuped_by')

@admin.register(File_Recovery)
class File_RecoveryAdmin(admin.ModelAdmin):
    list_display = ('recovery_file', 'recovery_status', 'created_at', 'recovery_location', 'recovered_by')

@admin.register(Notification_Token)
class Notification_TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'device_type', 'created_at', 'updated_at', 'is_active')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'message', 'notification_type' ,'notification_token', 'related_file', 'is_read', 'created_at')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')
