from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index' ),
    url(r'^sc_music/$', views.sc_music, name='sc_music'),
    url(r'^del_music/$', views.del_music, name='del_music'),

    url(r'^duanzi/$',views.duanzi,name='duanzi' ),
    url(r'^sc_duanzi/$',views.sc_duanzi,name='sc_duanzi' ),
    url(r'^del_duanzi/$', views.del_duanzi, name='del_duanzi'),

    url(r'^tupian/$',views.tupian,name='tupian' ),
    url(r'^sc_tupian/$', views.sc_tupian, name='sc_tupian'),
    url(r'^del_tupian/$', views.del_tupian, name='del_tupian'),

    url(r'^liuyanban/$',views.liuyanban,name='liuyanban' ),
    url(r'^sc_liuyanban/$', views.sc_liuyanban, name='sc_liuyanban'),
    url(r'^del_liuyanban/$', views.del_liuyanban, name='del_liuyanban'),



    url(r'^queren/$',views.queren,name='queren'),

    url(r'^xiagu/$', views.xiagu, name='xiagu'),
    url(r'^sousuo/$', views.sousuo, name='sousuo'),




]
