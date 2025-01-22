#front/urls.py 
from django.urls import path, re_path
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
    path('get-data/', views.get_data),
    path('add-data/', views.add_data),
    path('get-data/<int:data_id>/', views.get_data_by_id),
    path('update-data/<int:data_id>/', views.update_data_by_id),
    path('delete-data/<int:data_id>/', views.delete_data_by_id),
    #re_path(r'^(?P<menu_id>[0-9]{2}+)/$', views.menu_by_id),
]