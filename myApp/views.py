from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home(request):
    #product = Product.objects.all()
    #context = {'products':products}
    #return render(request, 'myApp/home.html', context)

    item1 = "iPhone 14"
    item2 = "Macbook"
    item3 = "Ipad"
    context = {"item1" :item1, "item2" :item2, "item3" : item3}
    return render(request, 'myApp/home.html',context)
    return HttpResponse('<h1>Hello World</h1>')