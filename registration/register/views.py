import email
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from django.contrib import messages

# Create your views here.

def LOGIN(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            name = User.objects.get(email=email).username
            print(name)
            user = authenticate(username=name, password=password)
            print('user')
            messages.success(request,"user authenticated")
            if user is not None:
                login(request, user)
                messages.success(request,"login success")
                return render(request,"website.html")
            else:  
                messages.success(request,"error please try again")  
                return redirect('regis')
        return render(request,'LOGIN.html')        
       
def LOGOUT(request):
     LOGOUT(request)
     messages.success(request,'logged out succesfully')
     return redirect('regis.html')

def regis(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        messages.success(request,'user created successfully')
        return redirect('LOGIN')
    else:
      return render(request,'regis.html')

def website(request):
     return render(request,'website.html')
