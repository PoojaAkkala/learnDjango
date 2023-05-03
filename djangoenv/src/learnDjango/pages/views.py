from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
# def homepage_view():
#     return HttpResponse("<h1>Hello World</h1>")

# class MyView(TemplateView):
#     template_name = 'myapp/index.html'

def home(request,*args,**kwargs):
    return render(request,'home.html')

def contact(request,*args,**kwargs):
    return render(request,'contact.html')

def about(request,*args,**kwargs):
    return render(request,'about.html')