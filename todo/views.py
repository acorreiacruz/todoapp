from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarefa
from .forms import Cadastrar


def listar_tarefas(request):
    tarefas = Tarefa.objects.filter(
        done = False,
    ).order_by('title')

    return render(request,"todo/pages/list.html",context={
        "tarefas": tarefas,
    })


def detalhar_tarefas(request, pk):
    tarefa = get_object_or_404(
        Tarefa.objects.all(),
        id = pk
    )

    return render(request, "todo/pages/detail.html", context={
        "tarefa": tarefa,
    })


def excluir_tarefa(request, pk):
    Tarefa.objects.filter(id = pk).delete()
    return redirect('/')


def finalizar_tarefa(request, pk):
    Tarefa.objects.filter(id=pk).update(done=True)
    return redirect('/')


def cadastrar_tarefas(request):
    dados_form = request.session.get('dados_form', None)
    form = Cadastrar(dados_form)

    return render(request, 'todo/pages/create.html', context={
        'form': form,
        'form_action': reverse('todo:cadastrar_validar'),
    })


def cadastrar_tarefas_validar(request):
    if not request.POST:
        return Http404()
    
    dados_form = request.POST
    request.session['dados_form'] = dados_form
    form = Cadastrar(dados_form)

    if form.is_valid():
        form.save()
        del(request.session['dados_form'])
    
    return redirect('todo:cadastrar')


