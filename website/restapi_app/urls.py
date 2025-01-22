from django.urls import path, include
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'restapi_app' 

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('get-data/', views.get_data),
    path('add-data/', views.add_data),
    path('get-data/<int:data_id>/', views.get_data_by_id),
    path('update-data/<int:data_id>/', views.update_data_by_id),
    path('delete-data/<int:data_id>/', views.delete_data_by_id),
]