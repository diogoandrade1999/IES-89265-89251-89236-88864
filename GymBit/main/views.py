from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import WorkModelSerializer, ExercisesModelSerializer, UserModelSerializer
from main.models import UserModel, WorkModel, ExercisesModel

from django.shortcuts import render


def index_view(request):
    return render(request, "index.html")


def trainees_view(request):
    return render(request, "trainees.html")


def charts_view(request):
    return render(request, "charts.html")


@api_view(['GET'])
def profile_view(request):
    #id = int(request.GET['id'])
    try:
        user = UserModel.objects.get(name='Diogo')
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserModelSerializer(user)
    return render(request, "profile.html", {'user': serializer.data})


def tables_view(request):
    return render(request, "tables.html")