from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from PyApp import user_decorator

# Create your views here.

from PyApp.models import *
from PyApp import models
from PyGood.models import GoodsInfo
from hashlib import sha1


# def register_exist(request):

# 注册页面
def register(request):
    context = {"title": "注册"}
    # 验证用户名是否存在
    name = request.GET.get('uname')
    if name != None:
        count = UserInfo.objects.filter(uname=name).count()
        return JsonResponse({'count': count})

    return render(request, 'register.html', context=context)


def register_handle(request):
    # print("123")
    post = request.POST
    user_name = post.get("user_name")
    pwd = post.get("pwd")
    cpwd = post.get("cpwd")
    email = post.get("email")
    if pwd != cpwd:
        return redirect('/register/')
    # 密码加密
    # s1 = sha1()
    # s1.update(pwd)
    # pwd3 = s1.hexdigest().

    # 创建对象
    user = UserInfo()
    user.uname = user_name
    user.upwd = cpwd
    user.uemail = email
    user.save()
    # 注册成功，转的登录页面

    return Login_hander(request)


# 登录页面
def Login_hander(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'uname': uname}
    return render(request, 'login.html', context=context)


def LoginYan(request):
    post = request.POST
    name = post.get("username")
    pwd = post.get("pwd")
    jizhu = post.get("jizhu", 0)
    users = models.UserInfo.objects.filter(uname=name)
    # print(name)
    if len(users) == 1:
        if users[0].upwd == pwd:
            # request.session['user_name'] = name
            # url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect('/info/')

            # red = render(request,'user_center_info.html')
            if jizhu != 0:
                red.set_cookie('uname', name)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = name

            return red
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': name, 'upwd': pwd}
            return render(request, 'login.html', context=context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': name, 'upwd': pwd}
        return render(request, 'login.html', context=context)


# 退出并删除session的值
def logout(request):
    request.session.flush()
    return redirect('/')


# 个人中心


def info(request):
    cookiesgood = goods_ids = request.COOKIES.get('goods_id2', '')
    goods_list = []
    if cookiesgood != '':
        goods_ids = goods_ids.split(',')

        for good_id in goods_ids:
            goods_list.append(GoodsInfo.objects.get(id=int(good_id)))
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    user_prico = UserInfo.objects.get(id=request.session['user_id']).uphone
    context = {'title': '用户中心',
               'user_email': user_email,
               'user_name': request.session['user_name'],
               'user_cart': 1,
               'goods_list': goods_list,
               'user_prico': user_prico,
               }
    return render(request, 'user_center_info.html', context=context)


# 收货地址

def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title': '用户中心', 'user_cart': 1, 'user': user}
    return render(request, 'user_center_site.html', context=context)
