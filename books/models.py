from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserInfo(models.Model):
    user = models.OneToOneField(User,primary_key=True)

class BookInfo(models.Model):
    isbn = models.CharField(max_length = 13)
    pic_url = models.URLField(max_length = 100,null=True,blank=True)
    title = models.CharField(max_length = 100,null=True,blank=True)
    pages = models.IntegerField(default = 0)
    author = models.CharField(max_length = 100,null=True,blank=True)
    price = models.CharField(max_length = 20)
    publisher=models.CharField(max_length=100,null=True,blank=True)
    pubdate = models.CharField(max_length=20,null=True,blank=True)
    has_data = models.BooleanField(default = False)
    doubanid= models.CharField(max_length = 20, null = True,blank=True)

class GoodsInfo(models.Model):
    seller = models.ForeignKey(User,related_name="goods")
    book = models.ForeignKey(BookInfo,related_name = "goods")
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quality = models.IntegerField(default = 100)
    description = models.CharField(max_length = 500, null = True, blank = True)
    sell_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True) 

#log some important system informaiton
#class SystemInfo(models.Model):
    #last_crawl_douban_time = models.DateTimeField(

