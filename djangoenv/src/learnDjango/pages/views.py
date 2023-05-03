from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
# def homepage_view():
#     return HttpResponse("<h1>Hello World</h1>")

# class MyView(TemplateView):
#     template_name = 'myapp/index.html'

def home(request):
    """
    View function for the home page.
    """
    context = {'message': 'Welcome to the home page!'}
    return HttpResponse("<h1>Hello World</h1>")
    # return render(request,'<h1>Hello World</h1>')