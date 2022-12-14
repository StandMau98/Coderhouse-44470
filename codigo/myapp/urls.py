from django.urls import path
from myapp.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', inicio, name='c-inicio'),
    path('palas/', PalasList.as_view(), name='c-palas'),
    path('palas/detail/<pk>', Palasdetail.as_view(), name='c-palas-detail'),
    path('palas/create/', PalasCreate.as_view(), name='c-palas-create'),
    path('palas/update/<pk>', PalasUpdate.as_view(), name='c-palas-update'),
    path('palas/delete/<pk>', PalasDelete.as_view(), name='c-palas-delete'),
    path('profesores/', profesores, name='c-profesores'),
    path('profesores/crear/', creacion_profesores, name='coder-profesores-crear'),
    path('torneo/', torneo, name='c-torneo'),
    path('torneo/delete/<id>/', delete_torneo, name='c-torneo-delete'),
    path('torneo/update/<id>/', update_torneo, name='c-torneo-update'),
    path('torneo/buscar/', buscar_torneo, name='coder-torneo-buscar'),
    path('torneo/buscar/resultados/', resultados_busqueda_torneo, name='coder-torneo-buscar-resultados'),
    path('contacto/', contacto, name='c-contacto'),

    path('login/', loguin_sesion, name='auth-login'),
    path('register/', register_user, name='auth-register'),

    path('logout/', LogoutView.as_view(template_name='myapp/logout.html'), name='auth-logout'),
    path('perfil/editar/', edit_perfil, name='auth-edit'),

    path('perfil/avatar/', agregar_avatar, name='auth-avatar')


    
]

#    path('torneo/crear/', creacion_torneo, name='coder-torneo-crear'),