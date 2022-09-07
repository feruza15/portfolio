from django.contrib import admin
from .models import Home, SendMessage, Student
# Register your models here.


class SendModelMessage(admin.ModelAdmin):
    list_display=('name', 'email', 'subject', 'message')
admin.site.register(SendMessage, SendModelMessage)
admin.site.register(Home)

class StudentModel(admin.ModelAdmin):
    list_display=('name', 'email', 'username', 'password1', 'password2')
admin.site.register(Student, StudentModel)