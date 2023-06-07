from django.shortcuts import render
from contact.models import form
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def contact(request): 
    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        enquiry = request.POST.get('enquiry')
        p=form(firstname=firstname,lastname=lastname,email=email,phone=phone,enquiry=enquiry)
        print(email)
        send_mail("contact us",enquiry , settings.EMAIL_HOST_USER , [email])
        p.save()
        print(firstname,lastname,email,phone,enquiry)
    return render(request,'contact.html')