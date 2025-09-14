from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request,'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    
        user = User.objects.filter(username = username).first()

        if user:
            return HttpResponse('Usuario já existe')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HttpResponse('Usuario cadastrado com sucesso')
        
    
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return HttpResponse('Authenticado')
        else:
            return HttpResponse(' Email ou senha invalidos')