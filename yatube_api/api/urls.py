from django.urls import include, path
from rest_framework.authtoken import views

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]