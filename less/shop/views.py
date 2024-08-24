from django.shortcuts import render
from django.http import HttpResponse
from .models import Product# this will import defined Product from models.py
from  math import ceil


def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    nSlides=n//4+ ceil((n/4)-(n//4))
    #params ={'no_of_slides':nSlides,'range':range(1,nSlides),'product':products}
    allProds=[[products,range(1,nSlides),nSlides],
             [products,range(1,nSlides),nSlides]]
    params={'allProds':allProds}
              
    return render(request,'shop/index.html',params)


def about(request):
    return render(request,'shop/about.html')


def contact(request):
    return HttpResponse("We are at Contact")


def tracker(request):
    return HttpResponse("We are at Tracker")


def search(request):
    return HttpResponse("We are at search")


def productView(request):
    return HttpResponse("We are at Product View")


def checkout(request):
    return HttpResponse("We are at Checkout")


def productlist(request):
    context = {
        'product':Product.objects.all()
    }
    return render(request,'shop/product.html',context)

