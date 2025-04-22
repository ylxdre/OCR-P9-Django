from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django import forms
from authentication.forms import LoginForm, RegisterForm


def login_page(request):
    form = LoginForm() 
    message = ""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    )
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            message = "Identifiants invalides"

    print(request.POST)
    
    return render(request, 
            'authentication/login.html',
            {'form': form})


def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/register.html', {'form': form})
