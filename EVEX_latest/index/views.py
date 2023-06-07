from django.shortcuts import render
#from index.models import prod
# Create your views here.

def index(request):
     # index=prod.objects.all()
     # data={'product':index}
     return render(request,'index.html')

