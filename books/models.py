from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class JTest(models.Model):
    jtest = models.CharField(max_length = 100)
    jtest2 = models.CharField(max_length = 100)

class UserInfo(models.Model):
    user = models.OneToOneField(User,primary_key=True)

class BookInfo(models.Model):
    isbn = models.CharField(max_length = 13)
    pic_url = models.URLField(max_length = 100,null=True,blank=True)
    title = models.CharField(max_length = 100,null=True,blank=True)
    pages = models.IntegerField(default = 0)
    author = models.CharField(max_length = 100,null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places =2,default = 0)
    publisher=models.CharField(max_length=100,null=True,blank=True)
    publidate = models.CharField(max_length=20,null=True,blank=True)
    has_data = models.BooleanField(default = False)

class GoodsInfo(models.Model):
    seller = models.ForeignKey(User)
    book = models.ForeignKey(BookInfo)
    price = models.DecimalField(max_digits=10,decimal_places=2)

#log some important system informaiton
#class SystemInfo(models.Model):
    #last_crawl_douban_time = models.DateTimeField(

