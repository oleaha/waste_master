from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.api.models import Container


@require_http_methods(['GET', 'POST'])
def login_view(request, *args, **kwargs):

    if request.method == 'POST':
        username = request.POST['in_username']
        password = request.POST['in_password']

        user = authenticate(username=username, password=password)

        if not user:
            messages.add_message(request, messages.ERROR, "Illegal username and or password")
            return render(request, "frontend/login.html", {'username': username})

        if user.is_active:
            login(request, user)
            return redirect("profile")
        else:
            messages.add_message(request, messages.ERROR, "Your user is deactivated")
            return render(request, "frontend/login.html", {'username': username})
    else:
        if request.user.is_authenticated():
            return redirect("profile")
        return render(request, "frontend/login.html")



@login_required
@require_http_methods(['GET', 'POST'])
def calculate_route_view(request, *args, **kwargs):

    containers = Container.objects.all()

    if request.method == 'POST':
        team = request.POST['team']

        return render(request, "frontend/calculate_route.html", {
            'containers': containers,
            'showGenerated': True,
            'team': team,
        })

    return render(request, "frontend/calculate_route.html", {
        'containers': containers
    })


@require_GET
@login_required
def request_rtl_view(request, *args, **kwargs):
    return render(request, "frontend/request-rtl.html")


@require_GET
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request):
    return render(request, "frontend/main.html")