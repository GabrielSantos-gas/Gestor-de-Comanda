from django.urls import path, include
from django.contrib.auth import views as auth_views
from gestorcomanda.views import listar_comandas, adicionar_item, editar_comanda, criar_comanda, detalhes_comanda, excluir_comanda, excluir_item, buscar_comandas, register_view, logout_view


urlpatterns = [
    path('login/account/', auth_views.LoginView.as_view(), name='login_account'),
    # Outras URLs de autenticação e do seu app
    path('', include('gestorcomanda.urls')),  # Adicione isso se você incluir suas outras URLs em um arquivo gestorcomanda/urls.py
]
