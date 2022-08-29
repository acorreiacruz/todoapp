from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from ..models import Tarefa
from ..forms import Cadastrar


def get_tarefa_object(pk):
    return Tarefa.objects.filter(pk=pk)


def listar_tarefas(request):
    tarefas = Tarefa.objects.filter(
        done=False,
    ).order_by('title')

    return render(request, "todo/pages/list.html", context={
        "tarefas": tarefas,
    })


def detalhar_tarefas(request, pk):
    tarefa = get_object_or_404(
        Tarefa.objects.all(),
        id=pk
    )

    return render(request, "todo/pages/detail.html", context={
        "tarefa": tarefa,
    })


def editar_tarefas(request, pk):
    get_tarefa_object(pk).update(
        title=request.POST.get('title'),
        description=request.POST.get('description')
    )
    return redirect('/')


def excluir_tarefa(request, pk):
    get_tarefa_object(pk).delete()
    return redirect('/')


def finalizar_tarefa(request, pk):
    get_tarefa_object(pk).update(done=True)
    return redirect('/')


def cadastrar_tarefas(request):
    dados_form = request.session.get('dados_form', None)
    form = Cadastrar(dados_form)

    return render(request, 'todo/pages/create.html', context={
        'form': form,
        'form_action': reverse('todo:cadastrar_validar')
    })


def cadastrar_tarefas_validar(request):
    if not request.POST:
        raise Http404()

    dados_form = request.POST
    request.session['dados_form'] = dados_form
    form = Cadastrar(dados_form)

    if form.is_valid():
        form.save()
        del(request.session['dados_form'])
        return redirect('/')

    return redirect('todo:cadastrar')


def buscar_tarefas(request):

    q = request.GET.get('q', '')
    tarefas = Tarefa.objects.filter(
        done=False,
        title__icontains=q
    )

    return render(request, 'todo/pages/list.html', context={
        'tarefas': tarefas,
    })
