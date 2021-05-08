from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Car

# Create your views here.


def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    cars = Car.objects.all()
    return render(request, 'dashboard.html', {'cars': cars})


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
