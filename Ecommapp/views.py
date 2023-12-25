from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"header.html")
def About(request):
    return HttpResponse("About")
def Account(request):
    return HttpResponse("Account")
def Order(request):
    return HttpResponse("Order")
def Card(request):
    return HttpResponse("Card")