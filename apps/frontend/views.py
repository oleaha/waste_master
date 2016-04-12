from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@require_http_methods(['GET', 'POST'])
def login_view(request, *args, **kwargs):

    if request.method == 'POST':
        username = request.POST['in_username']
        password = request.POST['in_password']

        user = authenticate(username=username, password=password)

        if not user:
            messages.add_message(request, messages.ERROR, "Ugyldig brukernavn eller passord")
            return render(request, "frontend/login.html", {'username': username})

        if user.is_active:
            login(request, user)
            return redirect("profile")
        else:
            messages.add_message(request, messages.ERROR, "Brukeren er deaktivert")
            return render(request, "frontend/login.html", {'username': username})
    else:
        if request.user.is_authenticated():
            return redirect("profile")
        return render(request, "frontend/login.html")


@require_GET
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request):
    return render(request, "frontend/main.html")