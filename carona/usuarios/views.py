# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Usuario
from .forms import CadastroForm, LoginForm, PerfilForm

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['senha'])
            if usuario:
                auth_login(request, usuario)
                return redirect('perfil')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def perfil(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = PerfilForm(instance=request.user)
    return render(request, 'usuarios/perfil.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')