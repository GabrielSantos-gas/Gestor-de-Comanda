from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from gestorcomanda.views import listar_comandas, adicionar_item, editar_comanda, criar_comanda, detalhes_comanda, excluir_comanda, excluir_item, buscar_comandas, register_view, logout_view
from django.views.static import serve
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', listar_comandas, name='listar_comandas'),
    path('comanda/<int:comanda_id>/adicionar_item/', adicionar_item, name='adicionar_item'),
    path('comanda/<int:comanda_id>/editar_comanda/', editar_comanda, name='editar_comanda'),
    path('criar_comanda/', criar_comanda, name='criar_comanda'),
    path('comanda/<int:comanda_id>/', detalhes_comanda, name='detalhes_comanda'),
    path('comanda/<int:comanda_id>/excluir_comanda/', excluir_comanda, name='excluir_comanda'),
    path('comanda/<int:comanda_id>/excluir_item/<int:item_id>/', excluir_item, name='excluir_item'),
    path('buscar_comandas/', buscar_comandas, name='buscar_comandas'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('', include('gestorcomanda.urls')),
]