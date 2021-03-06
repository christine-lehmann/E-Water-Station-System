from django.conf.urls import url 
from EWater_api import views

urlpatterns = [ 

    ### Orderslip session builder route
    url(r'^orderslip/order$', views.client_info_builder, name='order'),

    #### Client routes ###
    url(r'^api/client$', views.client_list),
    url(r'^api/client/(?P<pk>[0-9]+)$', views.client_detail),
    url(r'^api/client/verified$', views.Client_list_verified),

    ### Order routes ###
    url(r'^api/orders$', views.order_list),
    url(r'^api/orders/(?P<pk>[0-9]+)$', views.order_detail),
    url(r'^api/orders/paid$', views.Order_list_paid),
    url(r'^api/orders/delivered$', views.Order_list_delivered),

    ### Order status routes ###
    url(r'^api/orders/status$', views.order_status_list),
    url(r'^api/orders/status/(?P<pk>[0-9]+)$', views.order_status_detail),

    ### Statistics routes ###
    url(r'^api/statistics$', views.order_stats_list),
    url(r'^api/statistics/(?P<pk>[0-9]+)$', views.order_stats_detail),
]