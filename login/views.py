from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse,Http404
#from login.serializers import login_pageSerializer,registration_pageSerializer
from django.http import HttpResponse, JsonResponse



# Create your views here.

def home(request):
    return render(request,'index.html')

def all_details(request):
    data=User.objects.all()
    return render(request, 'all_details.html',{'data':data})

def all_users(request):
    print("___________________________________________")
    data= User.objects.all()
    return render(request,'all_users.html',{'data':data})
    
def user_details(request, username):
    data=User.objects.get(username=username)   
    return render(request,'details.html',{'data': data})   

def login(request):
    if request.method=='POST':

        user=authenticate(request,username=request.POST['username'] , password=request.POST['password'])
        if user is not None:
            #login(request,user)
            return render(request,'logout.html',{'data':request.GET['username']})
        else: 
            return HttpResponse('<h1> worng data Entry </h1> <button type="signup"><a href="/signup/">Logout</a></button> ')
    else:
        return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        User.username=request.POST['username']
        User.first_name=request.POST['first_name']
        User.last_name=request.POST['last_name']
        User.email=request.POST['email']
        User.password=request.POST['password']
        x=User()
        x.save()
        return redirect('/login/')
    if request.method=='GET':
        return render(request,'signup.html')