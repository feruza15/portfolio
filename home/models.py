from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class SendMessage(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=150, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=50, null=True)