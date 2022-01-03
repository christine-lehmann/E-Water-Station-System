from django.conf.urls import url 
from EWater_api import views

urlpatterns = [ 
    url(r'^api/client$', views.client_list),
    url(r'^api/client/(?P<pk>[0-9]+)$', views.client_info),
]
