from django.shortcuts import render,redirect
from django.http import JsonResponse
from PyCart.models import CartInfo
from PyApp.views import UserInfo

# Create your views here.

# 购物车页面
def GoodCart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {'title': '购物车','user_cart':1,'carts':carts,}
    return  render(request,'cart.html',context=context)


def add(request,gid,count):
    # 用户uid购买gid商品，数量为count
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)

    # 判断购物车中是否存在商品，如果存在就删除，没有就添加
    carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()

    # 如果是Ajax请求则返回json,否则转向购物车
    if request.is_ajax():
        count =CartInfo.objects.filter(user_id=request.session["user_id"]).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')




def edit(request,cart_id,count):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        count1 = cart.count = int(count)
        cart.save()
        data = {'ok':0}
    except Exception as e:
        data = {'ok':count1}
    return JsonResponse(data)



def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {'ok',1}
    except Exception as e:
        data = {'ok':0}
    return JsonResponse(data)










