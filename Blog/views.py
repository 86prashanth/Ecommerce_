from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http.response import JsonResponse
# Create your views here.
def home(request):
    return render(request,'blog/index.html')

def collection(request):
    category=Category.objects.filter(status=0)
    return render(request,'category/category.html',{'category':category})

def collectionview(request,slug):
    if(Category.objects.filter(status=0,slug=slug)):
        product=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={'product':product,'category':category}
        return render(request,'category/categoryview.html',context)
    else:
        messages.warning(request,'no such category found')
        
        
def productview(request,cat_slug,prod_slug):
    if(Category.objects.filter(slug=cat_slug,status=0)):
        if(Product.objects.filter(slug=prod_slug,status=0)):
            product=Product.objects.filter(slug=prod_slug,status=0).first
            context={'product':product}
        else:
            messages.error(request,'No such prooduct found')
            return redirect('collection')
    else:
        messages.error(request,'no such category found')
        return redirect('collection')
    return render(request,'product/product_view.html',context)

def product_list(request):
    products=Product.objects.filter(status=0).values_list("name",flat=True)
    productlist=list(products)
    return JsonResponse(productlist,safe=False)

