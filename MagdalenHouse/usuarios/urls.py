from django.urls import path


from .views import *

urlpatterns = [
    #USUARIOS
    path('', UsuarioView.as_view(), name='index-usuarios'),
    path('usuario/nuevo-usuario', CreateUserView.as_view(), name='crear-usuario'),
    path('usuario/editar-usuario/<int:pk>', EditUserView.as_view(), name='editar-usuario'),
    path('<int:pk>/password/', PasswordUserView.as_view(), name='password'),

    #GRUPOS
    path('grupo/', GroupView.as_view(), name='index-groups'),
    path('grupo/nuevo-grupo', CreateGroupView.as_view(), name='crear-grupo'),
]