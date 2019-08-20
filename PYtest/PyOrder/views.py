from django.shortcuts import render
from PyCart.models import UserInfo
from PyCart.models import CartInfo
from PyGood.models import GoodsInfo
from PyOrder.models import OrderDetatilInfo,OrderInfo
from django.http import JsonResponse
import datetime
import random



# Create your views here.



# 提交订单
def place(request):
    uid = request.session['user_id']
    user = UserInfo.objects.get(id= uid)
    carts = CartInfo.objects.filter(user_id=uid)

    context = {"title":"提交订单", 'user_place':1,'user':user,'carts':carts}
    return  render(request,'place_order.html',context=context)


# 添加订单表
def order(request):
    user = request.session["user_id"]
    Ordertext = OrderInfo()
    if request.is_ajax():
        goodid =  request.POST.get("id")
        list1 = str(goodid).split(",")
        goodcount = request.POST.get("count")
        Userin = UserInfo.objects.get(id=user)
        oid1 = random.randint(10000, 999999)
        oid2 = random.randint(10000, 999999)
        ototal = request.POST.get("ototal")
        intoid = "sj100sdf%s%s%s%s"%(oid1,user,oid2,Userin.uphone)
        Ordertext.oid =  intoid #+oid1+""+ user +"" +oid2 +""+ Userin.uphone
        Ordertext.user_id = user
        Ordertext.odate =datetime.datetime.now()
        Ordertext.oIsPay = False
        Ordertext.ototal = ototal # 实际的总价
        Ordertext.oaddress = Userin.uaddress
        order = OrderDetatilInfo()
        for i in list1:
            if i != "":
                good1 = CartInfo.objects.get(id=i)
                good2 = GoodsInfo.objects.get(id =good1.goods_id)
                order.goods.id = good2.id
                order.order.oid = intoid
                order.price = good2.gprice
                order.count = goodcount
                order.save()
        Ordertext.save()
        return JsonResponse({"data": 1})

    context= {'title':'用户中心','user_cart':1}
    return render(request, 'user_center_order.html', context=context)





