"""PYtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from PyApp.views import register,register_handle,Login_hander,LoginYan,info,site

from PyGood.views import GoodIndex,GoodDetail,GoodList

from PyCart.views import GoodCart,add,edit,delete

from PyOrder.views import place,order

urlpatterns = [
    # 用户界面
    path('admin/', admin.site.urls),
    path('register/', register),
    path('register_handle/', register_handle),
    path('Login/', Login_hander),
    path('LoginYan/', LoginYan),
    path('info/', info),
    path('order/', order),
    path('site/', site),




    # 商品界面

    url('^$', GoodIndex),
    url('^(\d+)/$', GoodDetail),
    url('^list(\d+)_(\d+)_(\d+)/$', GoodList),



    #购物车界面
    url('^cart/$', GoodCart),
    url('^cart/add(\d+)_(\d+)/$', add),
    url('^cart/edit(\d+)_(\d+)/$', edit),
    url('^cart/delete(\d+)/$', delete),

    # 订单页面
    path('place/', place),




    url('tinymce/', include('tinymce.urls')),



]
