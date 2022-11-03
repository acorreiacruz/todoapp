import os
from ..models import Tarefa
from ..forms import Cadastrar
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from utils.pagination import criar_paginacao
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render


PER_PAGE = int(os.environ.get('PER_PAGE', 6))


def get_tarefa_object(pk):
    return Tarefa.objects.filter(pk=pk)


@login_required(login_url='usuarios:login', redirect_field_name='next')
def listar_tarefas(request):
    tarefas = Tarefa.objects.filter(
        done=False,
        author=request.user
    ).order_by('title')

    pagina_objeto, range_de_paginacao = criar_paginacao(
        request,
        tarefas,
        PER_PAGE,
        quantidade_de_paginas=4
    )

    return render(request, "todo/pages/list.html", context={
        "tarefas": pagina_objeto,
        "range_de_paginacao": range_de_paginacao
    })


@login_required(login_url='usuarios:login', redirect_field_name='next')
def detalhar_tarefas(request, pk):
    tarefa = get_object_or_404(
        Tarefa.objects.all(),
        id=pk,
        author=request.user
    )

    return render(request, "todo/pages/detail.html", context={
        "tarefa": tarefa,
    })


@login_required(login_url='usuarios:login', redirect_field_name='next')
def editar_tarefas(request, pk):
    get_tarefa_object(pk).update(
        title=request.POST.get('title'),
        description=request.POST.get('description'),
        author=request.user
    )

    messages.success(request, "Tarefa editada com sucesso !")
    return redirect('/')


@login_required(login_url='usuarios:login', redirect_field_name='next')
def excluir_tarefa(request, pk):
    get_tarefa_object(pk).delete()
    messages.success(request, "Tarefa excluída com sucesso !")
    return redirect('/')


@login_required(login_url='usuarios:login', redirect_field_name='next')
def finalizar_tarefa(request, pk):
    get_tarefa_object(pk).update(done=True)
    messages.success(request, "Tarefa finalizada com sucesso !")
    return redirect('/')


@login_required(login_url='usuarios:login', redirect_field_name='next')
def cadastrar_tarefas(request):
    dados_form = request.session.get('dados_form', None)
    form = Cadastrar(dados_form)

    return render(request, 'todo/pages/create.html', context={
        'form': form,
        'form_action': reverse('todo:cadastrar_validar')
    })


@login_required(login_url='usuarios:login', redirect_field_name='next')
def cadastrar_tarefas_validar(request):
    if not request.POST:
        raise Http404()

    dados_form = request.POST
    request.session['dados_form'] = dados_form
    form = Cadastrar(dados_form)

    if form.is_valid():
        form.save()
        del(request.session['dados_form'])
        messages.success(request, "Nova tarefa criada com sucesso !")
        return redirect('/')

    messages.error(request, "Erro ao tentar criar a tarefa !")
    return redirect('todo:cadastrar')


@login_required(login_url='usuarios:login', redirect_field_name='next')
def buscar_tarefas(request):

    q = request.GET.get('q', '')
    tarefas = Tarefa.objects.filter(
        done=False,
        title__icontains=q
    )

    pagina_objeto, range_de_paginacao = criar_paginacao(
        request,
        tarefas,
        PER_PAGE,
        quantidade_de_paginas=4
    )

    return render(request, 'todo/pages/search.html', context={
        "termo_buscado": q,
        "tarefas": pagina_objeto,
        "range_de_paginacao": range_de_paginacao,
        "query_string_de_busca": f"q={q}&"
    })
