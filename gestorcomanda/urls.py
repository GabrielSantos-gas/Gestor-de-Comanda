
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_comandas, name='listar_comandas'),
    path('comanda/<int:comanda_id>/adicionar_item/', views.adicionar_item, name='adicionar_item'),
    path('comanda/<int:comanda_id>/editar_comanda/', views.editar_comanda, name='editar_comanda'),
    path('criar_comanda/', views.criar_comanda, name='criar_comanda'),
    path('comanda/<int:comanda_id>/', views.detalhes_comanda, name='detalhes_comanda'),
    path('comanda/<int:comanda_id>/excluir_comanda/', views.excluir_comanda, name='excluir_comanda'),
    path('comanda/<int:comanda_id>/excluir_item/<int:item_id>/', views.excluir_item, name='excluir_item'),
    path('buscar_comandas/', views.buscar_comandas, name='buscar_comandas'),
    path('comanda/<int:comanda_id>/excluir_comanda/', views.excluir_comanda, name='excluir_comanda'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),


]
