"""
URL configuration for learnDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views
from products.views import product_detail_view,product_create_view,dynamic_lookup_view,product_delete_view
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('product/', product_detail_view, name='about'),
    path('create/', product_create_view, name='about'),
    path('products/<int:id>/', dynamic_lookup_view, name='about'),
    path('products/<int:id>/delete/', product_delete_view, name='about'),
    path('admin/', admin.site.urls),
]
