from django.shortcuts import render,redirect
from django.conf import settings 
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
import uuid
from .models import *

# Create your views here.
def signup(request):
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password =  request.POST.get('password') 
        
        if User.objects.filter(email=email).first():
            return redirect('/signin')

        if User.objects.filter(username = username).first():
            return redirect('/signin')
       
        user_obj = User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        obj=User(username=username,email=email,password=password)
        send_mail("signup",username, settings.EMAIL_HOST_USER , [email])
        # profile_obj = Reset.objects.get(user= user_obj,forgot_password_token= str(uuid.uuid4()))
        # profile_obj.save()
    return render(request,'signup.html')

