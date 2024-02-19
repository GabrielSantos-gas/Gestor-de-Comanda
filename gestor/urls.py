from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new
from django.conf import settings
from django.views.static import serve
from views import *

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', home, name='home'),  # Rota para a página inicial
    path('listar_comandas/', listar_comandas, name='listar_comandas'),
    path('adicionar_item/<int:comanda_id>/', adicionar_item, name='adicionar_item'),
    path('editar_comanda/<int:comanda_id>/', editar_comanda, name='editar_comanda'),
    path('criar_comanda/', criar_comanda, name='criar_comanda'),
    path('detalhes_comanda/<int:comanda_id>/', detalhes_comanda, name='detalhes_comanda'),
    path('excluir_comanda/<int:comanda_id>/', excluir_comanda, name='excluir_comanda'),
    path('excluir_item/<int:comanda_id>/<int:item_id>/', excluir_item, name='excluir_item'),
    path('buscar_comandas/', buscar_comandas, name='buscar_comandas'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)