from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'shop/index.html')


def about(request):
    return HttpResponse("We are at About")


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
