from main.serializers import WorkModelSerializer, UserModelSerializer
from main.models import UserModel, WorkModel, ChartModel

from rest_framework_mongoengine import viewsets


class TraineesView(viewsets.ModelViewSet):
    lookup_field = 'user_id'
    serializer_class = UserModelSerializer

    def get_queryset(self):
        return UserModel.objects.all()


class TraineesProfileView(viewsets.ModelViewSet):
    # lookup_field = 'user_id'
    serializer_class = WorkModelSerializer

    def get_queryset(self):
        return WorkModel.objects.all()


class ProfileView(viewsets.ModelViewSet):
    lookup_field = 'user_id'
    serializer_class = UserModelSerializer

    def get_queryset(self):
        return UserModel.objects.all()


class ChartView(viewsets.ModelViewSet):
    lookup_field = 'user_id'
    serializer_class = ChartModelSerializer

    def get_queryset(self):
        return ChartModel.objects.all()
