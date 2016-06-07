from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.api.models import Container, ContainerReading
from random import randint
import random
from datetime import date


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

    info = dict()
    containers = Container.objects.all()

    for container in containers:
        container.last_reading = ContainerReading.objects.filter(container=container).last()

    return render(request, "frontend/request-rtl.html", {'containers': containers})


@require_GET
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile_view(request):
    return render(request, "frontend/main.html")


@login_required
def usage_view(request):

    containers = []
    cities = ['Tunga', 'Gloshaugen', 'Sentrum', 'Ila', 'Moholt', 'Melhus', 'Solsiden', 'Nardo', 'Tiller']

    for i in range(0, 500):
        # What fill grade should the containers have?
        fill = randint(1, 100)
        # Pick a random place in trondheim
        rand_city = cities[randint(0, 8)]

        if fill > 80:
            level = 'danger'
        elif fill > 60:
            level = 'warning'
        elif fill > 40:
            level = 'info'
        else:
            level = 'success'

        # Create random data for datatable
        start_date = date.today().replace(day=1, month=4).toordinal()
        end_date = date.today().toordinal()
        random_day = date.fromordinal(random.randint(start_date, end_date))
        random_empty = date.fromordinal(random.randint(start_date, end_date))

        containers.append(
            {
                'name': 'Test ' + str(i),
                'location': rand_city,
                'last_reading': random_day,
                'fill_grade': fill,
                'fill_level': level,
                'last_empty': random_empty,
            }
        )

    return render(request, 'frontend/usage.html', {'containers': containers})
