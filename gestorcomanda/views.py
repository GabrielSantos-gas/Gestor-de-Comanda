from django.shortcuts import render, redirect
from .models import Comanda, Item
from .forms import ItemForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import JsonResponse
from .models import Item


    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('listar_comandas')  # Redirecionar para a página após o login
    else:
        form = AuthenticationForm()
        
    return render(request, 'registration/login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecionar para a página de login após o registro bem-sucedido
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')


@login_required
def adicionar_item(request, comanda_id):
    comanda = Comanda.objects.get(id=comanda_id)
    total = comanda.total
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            descricao = form.cleaned_data['descricao']
            valor = form.cleaned_data['valor']
            quantidade = form.cleaned_data['quantidade']
            total = comanda.total + (valor * quantidade)
            comanda.total = total
            comanda.save()
            Item.objects.create(comanda=comanda, descricao=descricao, valor=valor, quantidade=quantidade)
            return redirect('detalhes_comanda', comanda_id=comanda_id)
    else:
        form = ItemForm()
    return render(request, 'partials/adicionar_item.html', {'form': form, 'comanda': comanda})


@login_required
def listar_comandas(request):
    hoje = datetime.now().date()
    comandas = Comanda.objects.filter(excluida=False)
    return render(request, 'partials/listar_comandas.html', {'comandas': comandas})


@login_required
def criar_comanda(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            if Comanda.objects.filter(nome=nome).exists():
                messages.error(request, 'Já existe uma comanda com este nome. Por favor, escolha outro nome.')
            else:
                nova_comanda = Comanda(nome=nome, total=0, data=date.today())
                nova_comanda.save()
                return redirect('detalhes_comanda', comanda_id=nova_comanda.id)
    return render(request, 'partials/criar_comanda.html')


@login_required
def editar_comanda(request, comanda_id):
    comanda = Comanda.objects.get(id=comanda_id)
    itens = Item.objects.filter(comanda=comanda)
    total = comanda.total
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            descricao = form.cleaned_data['descricao']
            valor = form.cleaned_data['valor']
            quantidade = form.cleaned_data['quantidade']
            total = comanda.total + (valor * quantidade)
            comanda.total = total
            comanda.save()
            Item.objects.create(comanda=comanda, descricao=descricao, valor=valor, quantidade=quantidade)
            return redirect('editar_comanda', comanda_id=comanda_id)
    else:
        form = ItemForm()
    context = {
        'comanda': comanda,
        'itens': itens,
        'total': total,
        'form': form,
        'comanda_id': comanda_id,  # Adiciona o ID da comanda ao contexto
    }
    return render(request, 'partials/editar_comanda.html', context)



@login_required
def detalhes_comanda(request, comanda_id):
    comanda = Comanda.objects.get(id=comanda_id)
    return render(request, 'partials/detalhes_comanda.html', {'comanda': comanda})


@login_required
def excluir_comanda(request, comanda_id):
    comanda = Comanda.objects.get(id=comanda_id)
    comanda.delete()
    return redirect('listar_comandas')


@login_required
def excluir_item(request, comanda_id, item_id):
    item = Item.objects.get(id=item_id)
    comanda = Comanda.objects.get(id=comanda_id)
    total = comanda.total - item.valor
    comanda.total = total
    comanda.save()
    item.delete()
    return redirect('editar_comanda', comanda_id=comanda_id)

@login_required
def buscar_comandas(request):
    q = request.GET.get('q')
    if q:
        comandas = Comanda.objects.filter(nome__icontains=q)
    else:
        comandas = Comanda.objects.all()
    
    return render(request, 'partials/buscar_comandas.html', {'comandas': comandas, 'q': q})



def atualizar_quantidade_item(request, comanda_id, item_id, quantidade_id):
    if request.method == 'POST':
        try:
            quantidade = int(request.POST.get('quantidade'))
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Quantidade inválida'})

        try:
            item = Item.objects.get(pk=quantidade_id)
            item.quantidade = quantidade
            item.save()

            # Calcular o total da comanda após a atualização do item
            total = calcular_total_comanda(item.comanda)

            return JsonResponse({'success': True, 'total': total})
        except Item.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item não encontrado'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método não permitido'})

def calcular_total_comanda(comanda):
    total = 0
    for item_comanda in comanda.item_set.all():
        total += item_comanda.quantidade * item_comanda.valor
    return total



class MinhaViewProtegida(LoginRequiredMixin, View):
    login_url = 'login'  # URL para redirecionamento de login
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        # Lógica da view
        return redirect(request, 'listar_comandas.html')
    
   