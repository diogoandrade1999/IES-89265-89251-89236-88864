from main.models import WorkModel, ExercisesModel, UserModel
from rest_framework import serializers


class WorkModelSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = WorkModel
        fields = ('_id', 'user', 'type', 'machine', 'date', 'exercises', 'heartbeat')


class ExercisesModelSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = ExercisesModel
        fields = ('weight', 'repetitions')


class UserModelSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = UserModel
        fields = ('_id', 'weight', 'name', 'birth_date', 'start', 'email')


'''
class PersonalModelSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = PersonalModel
        fields = ('_id', 'name', 'password', 'email')
'''