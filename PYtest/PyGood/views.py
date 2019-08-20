from django.shortcuts import render, redirect
from PyGood import models
from django.core.paginator import Paginator


# Create your views here.


# 首页页面
def GoodIndex(request):
    typelist = models.TypeInfo.objects.all()
    typy0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    typy01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]

    typy1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    typy11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    typy2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    typy22 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    typy3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    typy33 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    typy4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    typy44 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    typy5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    typy55 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {'title': '首页', 'guest_cart': 1,
               'typy0': typy0, 'typy01': typy01,
               'typy1': typy1, 'typy11': typy11,
               'typy2': typy2, 'typy22': typy22,
               'typy3': typy3, 'typy33': typy33,
               'typy4': typy4, 'typy44': typy44,
               'typy5': typy5, 'typy55': typy55,
               }
    return render(request, 'index.html', context=context)


# 列表页
def GoodList(request, tid, pindex, sort):
    typeinfo = models.TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':  # 默认 最新
        goods_list = models.GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2':  # 价格
        goods_list = models.GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort == '3':  # 点击量
        goods_list = models.GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gkucun')

    paginator = Paginator(goods_list, 10)
    page = paginator.page(int(pindex))
    context = {'title': typeinfo.title, 'guest_cart': 1,
               'page': page,
               'paginator': paginator,
               'typeinfo': typeinfo,
               'sort': sort,
               'news': news, }
    return render(request, 'list.html', context=context)


# 商品详细
def GoodDetail(request, id):
    goods = models.GoodsInfo.objects.get(pk=int(id))
    typeinfo = models.TypeInfo.objects.get(id=goods.gtype_id)
    # 商品的点击量+1
    goods.gclick = goods.gclick + 1
    goods.save()
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {'title': goods.gtype.title, 'guest_cart': 1,
               'g': goods, 'news': news, 'id': id, 'typeinfo': typeinfo, }
    response = render(request, 'detail.html', context=context)

    # 浏览的商品
    print(goods.id)

    # request.COOKIES('goods_ids',goods.id)
    goods_ids = request.COOKIES.get('goods_id2', '')
    goods_id = '%d' % (goods.id)
    if goods_ids != '':  # 判断是否有浏览记录，如果有则继续判断
        goods_ids1 = goods_ids.split(',')
        if goods_ids1.count(goods_id) >= 1:  # 判断列表中是否存在
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0, goods_id)  # 添加到第一个
        if len(goods_ids1) >= 6:  # 判断列表中的长度是否为6个
            del goods_ids1[5]
        goods_ids = ','.join(goods_ids1)
    else:
        goods_ids = goods_id
    response.set_cookie('goods_id2', goods_ids)  # 写入cookie里
    return response

# 回到首页
# def index(request):
#     return redirect('/GoodIndex/')
