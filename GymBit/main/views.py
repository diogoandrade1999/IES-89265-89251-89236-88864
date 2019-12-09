from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import WorkModelSerializer, ExercisesModelSerializer, UserModelSerializer
from main.models import UserModel, WorkModel, ExercisesModel

from django.shortcuts import render
import io


@login_required
def index_view(request):
    return render(request, "index.html")


@login_required
def trainees_view(request):
    try:
        users = UserModel.objects.all()
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return render(request, "trainees.html", {'users': users})


@login_required
def charts_view(request):
    return render(request, "charts.html")


@login_required
def profile_view(request):
    try:
        user = User.objects.get(username=request.user)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return render(request, "profile.html", {'user': user})


@login_required
def tables_view(request):
    return render(request, "tables.html")


@login_required
def trainee_info_view(request, name):
    try:
        user = UserModel.objects.get(name=name)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return render(request, "trainee_profile.html", {'user': user})


def login_view(request):
    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=email).exists():
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return index_view(request)
    return render(request, "login.html")


@login_required
def log_out(request):
    logout(request)
    return login_view(request)


def register_view(request):
    return render(request, "register.html")
