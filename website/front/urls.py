#front/urls.py 
from django.urls import path
from . import views

app_name = 'front' 

urlpatterns = [
    path('', views.index, name='index'),
    path('faqs/', views.faqs, name='faqs'),
    path('contacts/', views.contacts, name='contacts'),
    path('career/', views.career, name='career'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms-conditions/', views.terms_conditions, name='terms-conditions'),
    path('cookie-policy/', views.cookie_policy, name='cookie-policy'),
]