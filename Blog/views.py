from django.shortcuts import render
from .models import *
from django.contrib import messages
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