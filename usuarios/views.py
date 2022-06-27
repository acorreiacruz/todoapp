from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Cadastrar


def cadastrar(request):
    dados_form = request.session.get('dados_form', None)
    form = Cadastrar(dados_form)
    return render(request, 'usuarios/pages/cadastrar.html', context={
        'form': form,
        'form_action': reverse('usuarios:cadastrar_validar')
    })


def cadastrar_validar(request):
    if not request.POST:
        raise Http404()

    dados_form = request.POST
    request.session['dados_form'] = dados_form
    form = Cadastrar(dados_form)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        form.save()
        del(request.session['dados_form'])

    return redirect('usuarios:cadastrar')
