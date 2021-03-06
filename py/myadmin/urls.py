"""py URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . views import views,userviews,typesviews,goodsviews,backviews

urlpatterns = [
    #后台首页
    url(r'^$', views.index,name='myadmin_index'),

    # 会员管理路由
    url(r'^user/add/$', userviews.add,name='myadmin_user_add'),
    url(r'^user/index/$', userviews.index,name='myadmin_user_list'),
    url(r'^user/delete/$', userviews.delete,name='myadmin_user_delete'),
    url(r'^user/edit/$', userviews.edit,name='myadmin_user_edit'),

    #商品分类路由
    url(r'^types/add/$', typesviews.add,name='myadmin_types_add'),
    url(r'^types/index/$', typesviews.index,name='myadmin_types_list'),
    url(r'^types/delete/$', typesviews.delete,name='myadmin_types_delete'),
    url(r'^types/edit/$', typesviews.edit,name='myadmin_types_edit'),


    #商品管理路由
    url(r'^goods/add/$', goodsviews.add,name='myadmin_goods_add'),
    url(r'^goods/index/$', goodsviews.index,name='myadmin_goods_list'),
    url(r'^goods/delete/$', goodsviews.delete,name='myadmin_goods_delete'),
    url(r'^goods/edit/$', goodsviews.edit,name='myadmin_goods_edit'),

    # 订单管理
    url(r'^back/list/$', backviews.list,name='myadmin_back_list'),

    url(r'^back/edit/$',backviews.edit,name='myadmin_back_edit'),

    url(r'^back/info/$',backviews.info,name='myadmin_back_info'),
    
    #后台登录
    url(r'^registers/$',views.registers,name='myadmin_registers'),

]