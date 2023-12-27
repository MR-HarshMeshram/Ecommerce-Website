from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")
def About(request):
    return render(request,"About.html")
def Account(request):
    return render(request,"Account.html")
def Order(request):
    return render(request,"Order.html")
def Card(request):
    return render(request,"cart.html")
    