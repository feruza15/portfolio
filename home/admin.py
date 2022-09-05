from django.contrib import admin
from .models import Home, SendMessage
# Register your models here.


class SendModelMessage(admin.ModelAdmin):
    list_display=('name', 'email', 'subject', 'message')
admin.site.register(SendMessage, SendModelMessage)
admin.site.register(Home)
