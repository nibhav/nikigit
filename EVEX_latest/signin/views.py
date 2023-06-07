from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate    
from django.contrib.auth.models import User   
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        if username=='new,nibhav,niki,nikita':
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                print('user login success with username')
                return redirect('index')
            else:
                print('usernam or pssword is incorrect')
        else:
            try:
                user=authenticate(username=User.objects.get(email=username),password=password)   
            except:
                user=authenticate(username=username,password=password)
            if user is not None:
                print(user)
                login(request, user)
                print('user login success with email')
                return redirect('/index')
            else:
                print('username and password is incorrect')
    return render(request,'signin.html')
     

#user_check = models.YourModelName.objects.filter((Q(email = user)|Q(username = user)), password = password
# if request.method == 'POST':
#         username = request.POST['username']
#         print(username)
#         password = request.POST['password']
           
#         if not username:
#             return redirect('signin')
#         user_obj = User.objects.filter(username=username).first()

#         if user_obj is None:
#             return redirect('signin')
                
#         user = authenticate(username=username,password=password)
           
#         if user is not None and user.is_active:
#             print('user login success')
#             return redirect('courses')
#         else:
#            return render(request,'signin.html')