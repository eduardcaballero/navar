from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/<int:pk>/', views.usuario_detalle, name='usuario_detalle'),
    path('usuario/registrar', views.create_usuario, name='registrar'),
    path('solicitud/crear', views.crear_solicitud, name='crear_solicitud'),
    path('usuario/<int:pk>/edit/', views.usuario_editar, name='usuario_editar'),
    path('usuario/<int:pk>/eliminar/', views.usuario_eliminar, name='usuario_eliminar'),
]