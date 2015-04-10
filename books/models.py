from django.db import models

# Create your models here.


class JTest(models.Model):
    jtest = models.CharField(max_length = 100)
    jtest2 = models.CharField(max_length = 100)
