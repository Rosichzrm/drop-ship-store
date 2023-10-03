
from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
]
