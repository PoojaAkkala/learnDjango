from django.shortcuts import render
from .models import Product
from .forms import ProductCreateForm, RawProductsForm
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context={'object':obj}
    return render(request,"products/detail.html",context)

# def product_create_view(request):
#     form =  RawProductsForm()
#     if request.method=="POST":
#         form =  RawProductsForm(request.POST)
#         if form.is_valid():
#             Product.objects.create(**form.cleaned_data)
#             print(form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {"form":form}
#     return render(request,"products/product_create.html",context)

def product_create_view(request):
    form=ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    context={'form':form}
    return render(request,"products/product_create.html",context)
