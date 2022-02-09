
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class OrderPageView(TemplateView):
    template_name = "order.html"

class OrderSlipPageView(TemplateView):
    template_name = "orderslip.html"
