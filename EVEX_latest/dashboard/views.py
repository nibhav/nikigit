from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from contact.models import form
from become_dealer.models import become_dealer
# Create your views here.

def dashboard(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        print(password)
        name = User.objects.get(email=email).username
 
        user = authenticate(username=name, password= password)
        if user is not None:
            print(user)
            login(request, user)
            #return redirect("/index1")
            return render(request,"index1.html")
    return render(request,"dashboard.html")

def index1(request):
    return render(request,"index1.html")

def all_contact(request):
    contact =form.objects.all()
    cont ={'contact':contact}
    print(cont)
    print(contact)
    return render(request,"all_contact.html",cont)

def all_dealer(request):
    deal=become_dealer.objects.all()
    dea={'deal':deal}
    print(deal)
    print(dea)
    return render(request,"all_dealer.html",dea)