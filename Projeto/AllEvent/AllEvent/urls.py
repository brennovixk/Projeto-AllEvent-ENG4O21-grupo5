# AllEvent/urls.py
from django.contrib import admin
from django.urls import path
from AllEvent import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Páginas principais
    path('', views.home, name='home'),
    path('lista/', views.lista_view, name='lista'),
    path('event/', views.event_view, name='event'),

    # Login / Logout / Cadastro
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro_view, name='cadastro'),

    # Páginas de Perfil (requerem login)
    path('perfil/', views.perfil_view, name='perfil'), # Página principal do perfil
    path('perfil/editar/', views.editar_dados_view, name='editar_dados'),
    path('perfil/favoritos/', views.favoritos_view, name='favoritos'),
    path('perfil/preferencias/', views.preferencias_view, name='preferencias'),
]