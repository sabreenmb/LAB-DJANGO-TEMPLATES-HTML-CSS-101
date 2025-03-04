from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
# Create your views here.



def home_view(request:HttpRequest):
    return render(request,"main/index.html")

def thems_view(request:HttpRequest):
    return render(request,"main/themes_page.html")

def html_intro_view(request:HttpRequest):
    return render(request,"main/html_itroduction.html")

def css_intro_view(request:HttpRequest):
    return render(request,"main/css_introduction.html")

def cv_view(request:HttpRequest):
    return render(request,"main/cv.html")

def ai_view(request:HttpRequest):
    return render(request,"main/ai.html")

def large_font_view(request:HttpRequest):
    response=redirect("main:home_view")
    response.set_cookie("font", "large",max_age=60*60)
    return response
def normal_font_view(request:HttpRequest):
    response=redirect("main:home_view")
    response.set_cookie("font", "large",max_age=-3600)
    return response


