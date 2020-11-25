from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
path('', dashboard, name='dashboard')
path('', auth_views.LoginView.as_view(), name='login')
]