# AllEvent/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Home
def home(request):
    return render(request, 'MeuSite/home.html')

# Login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            # Tenta encontrar o usuário pelo email
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "E-mail ou senha incorretos.")

    return render(request, 'MeuSite/login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Cadastro
def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "Senhas não conferem.")
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, "E-mail já cadastrado.")
            return redirect('cadastro')
        
        # Tenta criar um username único a partir do email
        username_base = email.split('@')[0]
        username = username_base
        sufixo = 1
        while User.objects.filter(username=username).exists():
             username = f"{username_base}{sufixo}"
             sufixo += 1
        
        user = User.objects.create_user(username=username, email=email, password=password, first_name=nome)
        login(request, user)
        return redirect('home')

    return render(request, 'MeuSite/cadastro.html')

# Perfil (página principal do perfil)
def perfil_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # Redireciona para 'editar_dados' como página padrão do perfil
    return redirect('editar_dados') 

# Editar Dados
def editar_dados_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = request.user
        if nome:
            user.first_name = nome
        if email:
            # Verifica se o novo email já não está em uso por OUTRO usuário
            if User.objects.filter(email=email).exclude(pk=user.pk).exists():
                messages.error(request, "Este e-mail já está em uso.")
                return redirect('editar_dados')
            user.email = email
            user.username = email # Atualiza o username para ser o email
            
        if senha:
            user.set_password(senha)
        user.save()
        messages.success(request, "Dados atualizados com sucesso!")
        return redirect('editar_dados')

    return render(request, 'MeuSite/editar-dados.html')

# Preferências
def preferencias_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'MeuSite/preferencias.html')

# Favoritos
def favoritos_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'MeuSite/favoritos.html')

# Lista
def lista_view(request):
    return render(request, 'MeuSite/lista.html')

# Evento
def event_view(request):
    return render(request, 'MeuSite/event.html')