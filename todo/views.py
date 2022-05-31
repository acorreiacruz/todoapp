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
    form = Cadastrar()
    return render(request, 'todo/pages/create.html', context={
        'form': form,
    })