from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, logout, authenticate
from django.db import IntegrityError
from . models import Caso
from . forms import CasoForm

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            auth_login(request, user)
            return redirect('home')


def home(request):
    return render(request, 'home.html', {})

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                auth_login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las Contraseñas no coinciden'
                })

def signout(request):
    logout(request)
    return redirect('home')


def caso(request):
    if request.method == 'POST':
        form = CasoForm(request.POST)
        if form.is_valid():
            form.save()
            # read the doc for `redirect` and change the destination to
            # something that makes sense for your app.
            # as to why we redirect, cf  https://en.wikipedia.org/wiki/Post/Redirect/Get
            return redirect("/")

    else:
        # GET request, present an empty form
        form = CasoForm() 
    return render(request, 'ing_caso.html', {"form": form})
