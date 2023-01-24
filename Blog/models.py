from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
def category(request,filename):
    original_filename =filename
    nowTime=datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    filename="%s.%s" % (nowTime.original_filename)
    return os.path.join('category/',filename)

class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(null=False,blank=False,upload_to='category/')
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")    
    trending=models.BooleanField(default=False,help_text="0-default,1-trending")    
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.CharField(max_length=150,null=False,blank=False)
    created_on=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

def product(request,filename):
    original_filename =filename
    nowTime=datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    filename="%s.%s" % (nowTime.original_filename)
    return os.path.join('product/',filename)

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(null=False,blank=False,upload_to='product')
    description=models.TextField(max_length=500,null=False,blank=False)
    small_description=models.CharField(max_length=250,null=False,blank=False)
    quantity=models.IntegerField()
    original_price=models.FloatField(null=False, blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")    
    trending=models.BooleanField(default=False,help_text="0-default,1-trending")  
    tag=models.CharField(max_length=250,null=False,blank=False)  
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.CharField(max_length=150,null=False,blank=False)
    created_on=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile')
    
    def __str__(self):
        return f'{self.user.username} Profile'