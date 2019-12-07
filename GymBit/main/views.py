from django.urls import reverse

from main.models import PollModel, ChoiceModel, DynamicPageModel
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect

#Simple views just for the initial testing ------------------


def index_view(request):
    return render(request, "index.html")


def trainees_view(request):
    return render(request, "trainees.html")


def charts_view(request):
    return render(request, "charts.html")


def profile_view(request):
    return render(request, "profile.html")


def tables_view(request):
    return render(request, "tables.html")