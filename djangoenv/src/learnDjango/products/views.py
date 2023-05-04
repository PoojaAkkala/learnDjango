from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.http import Http404
from .forms import ProductCreateForm, RawProductsForm
# Create your views here.
def product_delete_view(request,id):
    obj=get_object_or_404(Product,id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context={"object":obj}
    return render(request,"products/delete.html",context)


def dynamic_lookup_view(request,id):
    # try:
    #     obj=Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404 
    obj=get_object_or_404(Product,id=id)
    context={"object":obj}
    return render(request,"products/detail.html",context)

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
