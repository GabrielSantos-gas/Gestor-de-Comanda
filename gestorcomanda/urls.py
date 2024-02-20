from django.urls import path, include
from django.contrib.auth import views as auth_views
from gestorcomanda.auth_urls import urlpatterns as auth_urlpatterns
from gestorcomanda.views import *
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
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
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [path('login/account/', auth_views.LoginView.as_view(), name='login_account')]
urlpatterns += [path('auth/', include(auth_urlpatterns))]  # ou qualquer outro prefixo que você queira para suas URLs de autenticação
