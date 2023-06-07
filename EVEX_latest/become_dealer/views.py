from django.shortcuts import render
from become_dealer.models import become_dealer
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def become_dealer(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        website = request.POST.get('website')
        organization = request.POST.get('organization')
        city = request.POST['city']
        proposed_firm = request.POST.get('proposed_firm')
        gst_no = request.POST.get('gst_no')
        account_number = request.POST.get('account_number')
        ifsc_code = request.POST.get('ifsc_code')
        account_holder = request.POST.get('account_holder')
        p=become_dealer(full_name=full_name,mobile=mobile,email=email,website=website,organization=organization,
                 city=city,proposed_firm=proposed_firm,gst_no=gst_no,account_number=account_number,
                ifsc_code=ifsc_code,account_holder=account_holder)
        send_mail("contact us",full_name, settings.EMAIL_HOST_USER , [email],fail_silently=False)
        p.save()
        
        print(full_name,mobile,email,website,organization,city,proposed_firm,gst_no,account_number,ifsc_code,account_holder)
         
    return render(request,'become_dealer.html')