from django.urls import path 
from .views import HomePageView, AboutPageView, ServicesPageView,ContactPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('',HomePageView.as_view(), name='index'),
    path('services/',ServicesPageView.as_view(), name='services'),
    path('contact/',ContactPageView.as_view(), name='contact'),
]


