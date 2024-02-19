from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def listar_comandas(request):
    return render(request, 'partials/listar_comandas.html')


def adicionar_item(request, comanda_id):
    return render(request, 'partials/adicionar_item.html')


def editar_comanda(request, comanda_id):
    return render(request, 'partials/editar_comanda.html')


def criar_comanda(request):
    return render(request, 'partials/criar_comanda.html')


def detalhes_comanda(request, comanda_id):
    return render(request, 'partials/detalhes_comanda.html')


def excluir_comanda(request, comanda_id):
    return render(request, 'partials/excluir_comanda.html')


def excluir_item(request, comanda_id, item_id):
    return render(request, 'partials/excluir_item.html')


def buscar_comandas(request):
    return render(request, 'partials/buscar_comandas.html')


def register_view(request):
    return render(request, 'registration/register.html')


def logout_view(request):
    return render(request, 'registration/logout.html')

def login_views(request):
    return render(request, 'registration/login.html')
