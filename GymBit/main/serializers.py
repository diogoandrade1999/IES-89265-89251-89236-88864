from main.models import WorkModel, ExercisesModel, UserModel
from rest_framework import serializers


class WorkModelSerializer(serializers.Serializer):
    class Meta:
        model = WorkModel
        fields = ('user', 'type', 'machine', 'date', 'exercises')


class ExercisesModelSerializer(serializers.Serializer):
    class Meta:
        model = ExercisesModel
        fields = ('weight', 'repetitions')


class UserModelSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        fields = ('weight', 'name', 'birth_date', 'start', 'email')
