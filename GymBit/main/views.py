from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import WorkModelSerializer, ExercisesModelSerializer, UserModelSerializer

from django.shortcuts import render


def index_view(request):
    return render(request, "index.html")


def trainees_view(request):
    return render(request, "trainees.html")


def trainee_info_view(request):
    return render(request, "trainee_profile.html")


def charts_view(request):
    return render(request, "charts.html")


def profile_view(request):
    return render(request, "profile.html")


def tables_view(request):
    return render(request, "tables.html")


def login_view(request):
    return render(request, "login.html")


def register_view(request):
    return render(request, "register.html")
