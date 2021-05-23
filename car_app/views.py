from urllib import request

from Tools.scripts.make_ctype import method
from django.contrib import auth
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Car, logs
from .forms import checkout
from datetime import datetime


def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    if request.method == "GET":
        cars = Car.objects.all()
        return render(request, 'dashboard.html', {'cars': cars})
    else:
        postData = request.POST
        userid = postData.get('carid')
        carid = postData.get('userid')
        print(userid, carid)
        Log = logs(user_id=userid, car_id=carid)
        Log.save()
        cars = Car.objects.all()
        return render(request, 'dashboard.html', {'cars': cars})


def Booking(request, id):
    car = Car.objects.get(id=id)


def checkoutview(request, id):
    form = checkout(request.GET)
    if request.method == 'GET':
        car = Car.objects.get(id=id)
        return render(request, 'checkout.html', {'car': car, 'form': form})
    else:
        postData = request.POST
        rentedDate = postData.get('rentedDate')
        returnDate = postData.get('returnDate')
        userid = postData.get('userid')
        carid = postData.get('carid')
        rent = Car.objects.get(id=int(carid)).car_rent
        date_str1 = datetime.strptime(rentedDate, '%Y-%m-%d')
        date_str2 = datetime.strptime(returnDate, '%Y-%m-%d')
        date_diff = date_str2 - date_str1
        total_rent = date_diff * rent



        print(userid, carid, rentedDate, returnDate,rent,date_str1,date_str2,date_diff,total_rent)
        Log = logs(user_id=userid, car_id=carid, rentedDate=rentedDate, returnDate=returnDate)
        Log.save()
        return render(request, 'final.html',{'total_rent':total_rent})


def finalView(request):
    if request.method == 'GET':
        return render(request, 'final.html', {'form': form})
    else:
        pass


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
