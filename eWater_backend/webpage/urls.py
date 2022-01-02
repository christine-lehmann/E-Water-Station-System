# djangotemplates/example/urls.py

from django.conf.urls import url
from webpage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='index'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^order/$', views.OrderPageView.as_view(), name='order'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^orderslip/$', views.OrderSlipPageView.as_view(), name='orderslip'),
]