from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User, auth

# Create your views here.


def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        message = SendMessage(name=name, email=email, subject=subject, message=message)
        message.save()
        return redirect('/')


    return render(request, 'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login (request, user)
        return redirect('/')

    return render(request, 'auth/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user=student.objects.created_user
        username=username,
        email=email
        user.save()
    return redirect('/')