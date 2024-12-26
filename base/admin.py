from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User) 
admin.site.register(Department)
admin.site.register(File)
admin.site.register(User_Profile)
admin.site.register(Audit_Log)
admin.site.register(Feedback)
admin.site.register(Metadata)