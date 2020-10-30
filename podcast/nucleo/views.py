from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,"nucleo/home.html")

def primeroA(request):
    return render(request,"nucleo/1A.html")

def primeroB(request):
    return render(request,"nucleo/1B.html")

def terceroA(request):
    return render(request,"nucleo/3A.html")

def terceroB(request):
    return render(request,"nucleo/3B.html")