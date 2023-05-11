from django.shortcuts import render,redirect
from . models import *

# Create your views here.

def sign(request):
    return render(request,'sign.html')
def sign_valid(request):
    if request.method=='POST':
        username= request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        work=Register(username=username,email=email,password1=password1,password2=password2)
        work.save()
        logo=Login(username=username,password1=password1,type=0)
        logo.save()
        return render(request,'sign.html')
def log(request):

    return render(request,'login.html')
def login_valid(request):
    username = request.POST['username']
    password1=request.POST['password1']
    blue=Login.objects.get(username=username,password1=password1)
    if blue.type==0:
        request.session['username']=blue.username
        return render(request,'home.html')
    elif blue.type==1:
        request.session['username']=blue.username
        return render(request,'home.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def service(request):
    item=Service.objects.all()
    d={
        'key':item
    }
    return render(request,'service.html',d)
def project(request):
    a=Projects.objects.all()
    g={
        'pass':a
    }
    return render(request,'project.html',g)