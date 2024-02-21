from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from gestorcomanda.views import listar_comandas, adicionar_item, editar_comanda, criar_comanda, detalhes_comanda, excluir_comanda, excluir_item, buscar_comandas, register_view, logout_view
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('login/account/', auth_views.LoginView.as_view(), name='login'),
    # Outras URLs de autenticação e do seu app
    path('', include('gestorcomanda.urls')),
    # Adicione isso se você incluir suas outras URLs em um arquivo gestorcomanda/urls.py
]
