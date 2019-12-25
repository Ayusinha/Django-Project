from django.shortcuts import render,redirect
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.http import HttpResponse,Http404
#from login.serializers import login_pageSerializer,registration_pageSerializer
from django.http import HttpResponse, JsonResponse



# Create your views here.

def home(request):
    messages.info(request,'loaded Home page')
    return render(request,'index.html')

def all_details(request):
    data=User.objects.all()
    return render(request, 'all_details.html',{'data':data})

def all_users(request):
    #print("___________________________________________")
    data= User.objects.all()
    return render(request,'all_users.html',{'data':data})
    
def user_details(request, username):
    data=User.objects.get(username=username)   
    return render(request,'details.html',{'data': data})   

def login(request):
    if request.method=='POST':
        print(request.POST)
        
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username , password=password)

        if user is not None:
            #login(request,user)
            auth.login(request,user)
            messages.info(request,'Successfully Loginned')
            return render(request,'logout.html',{'data':username})
        else: 
            messages.info(request,'login again  or do signup')
            return HttpResponse('<h1> worng data Entry </h1> <button type="signup"><a href="/signup/">Signup</a></button> <h4>OR</h4> <button type="signin"><a href="/login/">Login</a></button> ' )
    else:
        return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        print(request.POST)
        #x=User()
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        
        user=User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name,)
        user.save()

        messages.info(request,'Registered new user')
        return redirect('/login/')

    if request.method=='GET':
        return render(request,'signup.html')