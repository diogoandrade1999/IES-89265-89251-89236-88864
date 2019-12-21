from datetime import datetime, date

import requests

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from rest_framework import status
from rest_framework.decorators import api_view

from GymBit_Client.settings import API_URL


def login_view(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index.html")
    return render(request, "login.html")


def register_view(request):
    return render(request, "register.html")


def calc_weeks(start_date):
    actual_date = str(date.today())
    d1 = datetime.strptime(actual_date, "%Y-%m-%d")
    d2 = datetime.strptime(start_date, "%Y-%m-%d")
    weeks = (d1 - d2).days / 7
    return weeks


@login_required
def index_view(request):
    # get the trainee from the api
    result = requests.get(API_URL + "trainees")
    users = []
    news = 0
    if result.status_code == status.HTTP_200_OK:
        users = result.json()
        for u in users:
            if calc_weeks(u['start']) < 5:
                news += 1
    return render(request, "index.html", {'total': len(users), 'total_1': len(users)-1, 'news': news})


@login_required
def charts_view(request, id):
    # get the trainee from the api
    result = requests.get(API_URL + "trainees/" + str(id))
    user = []
    if result.status_code == status.HTTP_200_OK:
        user = result.json()
    # get the trainee from the api
    result = requests.get(API_URL + "charts")
    work = []
    if result.status_code == status.HTTP_200_OK:
        data2 = result.json()
        count = 0
        for obj in data2:
            if obj['user_id'] == id:
                for o in obj['bits']:
                    try:
                        work.append({"label": str(count), "value": o})
                        count += 1
                    except ValueError:
                        pass
    return render(request, "charts.html", {'user': user, 'work': work[-200:]})


@login_required
def tables_view(request):
    return render(request, "tables.html")


@login_required
def logout_view(request):
    logout(request)
    return login_view(request)


@login_required
@api_view(['GET'])
def trainees_view(request):
    # get the trainee from the api
    result = requests.get(API_URL + "trainees/" + str(request.user.pk))
    users = []
    if result.status_code == status.HTTP_200_OK:
        user = result.json()
        if user['personal_trainer'] == 'True':
            # get all trainees from the api
            result = requests.get(API_URL + "trainees")
            if result.status_code == status.HTTP_200_OK:
                users = result.json()
                users.remove(user)
        else:
            users += [user]
    return render(request, "trainees.html", {'users': users})


@login_required
@api_view(['GET'])
def profile_view(request):
    # get the trainee from the api
    result = requests.get(API_URL + "trainees/" + str(request.user.pk))
    user = []
    if result.status_code == status.HTTP_200_OK:
        user = result.json()
    return render(request, "profile.html", {'user': user})


@login_required
@api_view(['GET'])
def trainee_info_view(request, id):
    # get the trainee from the api
    result = requests.get(API_URL + "trainees/" + str(id))
    user = []
    if result.status_code == status.HTTP_200_OK:
        user = result.json()
    # get the trainee from the api
    result = requests.get(API_URL + "trainee_profile")
    work = []
    if result.status_code == status.HTTP_200_OK:
        data = result.json()
        for obj in data:
            if obj['user_id'] == id:
                work.append(obj)
    return render(request, "trainee_profile.html", {'user': user, 'work': work})
