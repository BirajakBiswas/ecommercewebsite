from django.shortcuts import render
from django.http import HttpResponse
from .models import Product# this will import defined Product from models.py



def index(request):
    return render(request,'shop/index.html')


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

