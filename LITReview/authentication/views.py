from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from authentication.forms import RegisterForm


def register_page(request):
    """
    Create a User from the register form
    :param: request (POST with RegisterForm data)
    :return: write the User in DB
    """
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/register.html', {'form': form})
