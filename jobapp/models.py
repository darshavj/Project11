from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    type = models.IntegerField()
class Register(models.Model):
    username=models.CharField(max_length=250)
    email=models.EmailField()
    password1=models.CharField(max_length=10)
    password2=models.CharField(max_length=10)

class Service(models.Model):
    title=models.CharField(max_length=200)
    image=models.FileField()
    content=models.CharField(max_length=500)
class Projects(models.Model):
    name = models.CharField(max_length=250)
    project_image = models.FileField()
    description = models.CharField(max_length=500)
    duration = models.CharField(max_length=200)
    status = models.CharField(max_length=100)

