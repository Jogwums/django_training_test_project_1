from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


# Create your views here.
# def index(request):
#     # return HttpResponse('Hello World')
#     return render(request, 'pages/index.html')

# class based views 

class HomePageView(TemplateView):
    template_name = 'pages/index.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ServicesPageView(TemplateView):
    template_name = 'pages/services.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'