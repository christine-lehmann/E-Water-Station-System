from django.conf.urls import url 
from EWater_api import views

urlpatterns = [ 

    #### Client routes ###
    url(r'^api/client$', views.client_list),
    url(r'^api/client/(?P<pk>[0-9]+)$', views.client_detail),
    url(r'^api/client/verified$', views.Client_list_verified),

    ### Order routes ###
    url(r'^api/orders$', views.order_list),
    url(r'^api/orders/(?P<pk>[0-9]+)$', views.order_detail),
    url(r'^api/orders/paid$', views.Order_list_paid),
    url(r'^api/orders/delivered$', views.Order_list_delivered)
]