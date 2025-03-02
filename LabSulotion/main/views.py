from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.



def home_view(request:HttpRequest):
    return render(request,"main/index.html")

def html_intro_view(request:HttpRequest):
    return render(request,"main/html_itroduction.html")

def css_intro_view(request:HttpRequest):
    return render(request,"main/css_introduction.html")

def cv_view(request:HttpRequest):
    return render(request,"main/cv.html")

def ai_view(request:HttpRequest):
    return render(request,"main/ai.html")

