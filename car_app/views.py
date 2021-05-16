from urllib import request

from Tools.scripts.make_ctype import method
from django.contrib import auth
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Car, logs
from django.views import View
from django.utils.decorators import method_decorator


def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    if request.method == "GET":
        cars = Car.objects.all()
        return render(request, 'dashboard.html', {'cars': cars})
    else:
        postData = request.POST
        userid = postData.get('userid')
        carid = postData.get('carid')
        print(userid, carid)
        Log = logs(userid=userid, carid=carid)
        Log.save()
        cars = Car.objects.all()
        return render(request, 'dashboard.html', {'cars': cars})


def checkoutview(request):
    if request.method == 'GET':
        #cars = Car.objects.all()
        return render(request, 'checkout.html')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('login_url')
