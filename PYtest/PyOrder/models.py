from django.db import models
from PyApp.models import UserInfo
from PyGood.models import GoodsInfo

# Create your models here.



class OrderInfo(models.Model):
    oid = models.CharField(max_length=20,primary_key=True)  # 订单号
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    odate = models.DateTimeField(auto_now=True) # 购买的当前时间
    oIsPay = models.BooleanField(default=False) # 是否购买
    ototal = models.DecimalField(max_digits=6,decimal_places=2) # 实际支付的金额
    oaddress = models.CharField(max_length=100) # 地址


class OrderDetatilInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo,on_delete=models.CASCADE)
    order = models.ForeignKey(OrderInfo,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2) # 价格
    count = models.IntegerField()  # 数量










