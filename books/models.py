from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class JTest(models.Model):
    jtest = models.CharField(max_length = 100)
    jtest2 = models.CharField(max_length = 100)

class UserInfo(models.Model):
    user = models.OneToOneField(User,primary_key=True)

