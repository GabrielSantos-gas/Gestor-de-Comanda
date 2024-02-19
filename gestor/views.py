from django.shortcuts import render

def home(request):
    return render(request, 'base_template.html')


def listar_comandas(request):
    return render(request, 'gestorcomanda/partials/listar_comandas.html')


def adicionar_item(request, comanda_id):
    return render(request, 'gestorcomanda/partials/adicionar_item.html')


def editar_comanda(request, comanda_id):
    return render(request, 'gestorcomanda/partials/editar_comanda.html')


def criar_comanda(request):
    return render(request, 'gestorcomanda/partials/criar_comanda.html')


def detalhes_comanda(request, comanda_id):
    return render(request, 'gestorcomanda/partials/detalhes_comanda.html')


def excluir_comanda(request, comanda_id):
    return render(request, 'gestorcomanda/partials/excluir_comanda.html')


def excluir_item(request, comanda_id, item_id):
    return render(request, 'gestorcomanda/partials/excluir_item.html')


def buscar_comandas(request):
    return render(request, 'gestorcomanda/partials/buscar_comandas.html')


def register_view(request):
    return render(request, 'gestorcomanda/partials/register.html')


def logout_view(request):
    return render(request, 'gestorcomanda/partials/logout.html')
