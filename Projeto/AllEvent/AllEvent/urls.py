from django.contrib import admin
from django.urls import path, include
from core import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Login personalizado
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login"
    ),

    # Logout personalizado (pode redirecionar para home)
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page='home'),
        name="logout"
    ),

    # URLs do app core
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),

    path('perfil/', views.perfil_view, name='perfil'),
    path('perfil/editar/', views.editar_dados, name='editar_dados'),
    path('perfil/favoritos/', views.favoritos_view, name='favoritos'),
    path('perfil/preferencias/', views.preferencias_view, name='preferencias'),

    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/buscar/', views.buscar_eventos, name='buscar_eventos'),
    path('eventos/resultado/', views.resultado_busca, name='resultado_busca'),
    path('evento/<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
]

# Servir arquivos estáticos e mídia em DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
