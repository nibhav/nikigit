from django.shortcuts import render
from product.models import car
# Create your views here.

def product(request):
    product=car.objects.all()
    data={'product':product}
    return render(request,'product.html',data)
