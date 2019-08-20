from django.db import models
from PyApp.models import UserInfo
from PyGood.models import GoodsInfo



# Create your models here.

class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    goods = models.ForeignKey(GoodsInfo,on_delete=models.CASCADE)
    count = models.IntegerField()






