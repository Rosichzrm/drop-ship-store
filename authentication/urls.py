from django.contrib import admin
from django.urls import path, include

from authentication import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
