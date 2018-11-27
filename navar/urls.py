from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('perfil/<int:pk>/', views.perfil_detalle, name='perfil_detalle'),
    path('login', views.login, name='login'),
]