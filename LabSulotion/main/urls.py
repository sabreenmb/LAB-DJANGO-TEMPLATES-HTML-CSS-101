from django.urls import path
from . import views

app_name ='main'

urlpatterns=[
    path("html/introduction/",views.html_intro_view,name='html_intro'),
    path("css/introduction/",views.css_intro_view,name='css_intro'),
    path("careers/cv/",views.cv_view,name='cv'),
    path("article/ai/",views.ai_view,name='AI'),
    
    path("",views.home_view,name='home')

]