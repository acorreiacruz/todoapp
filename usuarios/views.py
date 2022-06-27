from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CadastrarForm, LoginForm


def cadastrar(request):
    dados_form = request.session.get('dados_form', None)
    form = CadastrarForm(dados_form)
    return render(request, 'usuarios/pages/cadastrar.html', context={
        'form': form,
        'form_action': reverse('usuarios:cadastrar_validar')
    })


def cadastrar_validar(request):
    if not request.POST:
        raise Http404()

    dados_form = request.POST
    request.session['dados_form'] = dados_form
    form = CadastrarForm(dados_form)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        form.save()
        del(request.session['dados_form'])

    return redirect('usuarios:cadastrar')


def login_view(request):
    dados_form = request.session.get('dados_form', None)
    form = LoginForm(dados_form)
    return render(request, 'usuarios/pages/login.html', context={
        'form': form,
        'form_action': reverse('usuarios:login_validar')
    })


def login_view_validar(request):
    if not request.POST:
        raise Http404()

    dados_form = request.POST
    request.session['dados_form'] = dados_form
    form = LoginForm(dados_form)

    if form.is_valid():
        ...
