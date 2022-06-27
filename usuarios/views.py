from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CadastrarForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


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
    form = LoginForm()
    return render(request, 'usuarios/pages/login.html', context={
        'form': form,
        'form_action': reverse('usuarios:login_validar')
    })


def login_view_validar(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        usuario_autenticado = authenticate(
            email=form.cleaned_data.get('email', ''),
            password=form.cleaned_data.get('password', '')
        )

        if usuario_autenticado is not None:
            messages.success(request, 'Você está logado!')
            login(request, usuario_autenticado)
        else:
            messages.error(request, 'Credenciais inválidas')
    else:
        messages.error(request, 'E-mail ou senha inválidos!')

    return redirect('usuarios:login')
