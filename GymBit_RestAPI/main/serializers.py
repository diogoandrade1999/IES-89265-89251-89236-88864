from main.models import WorkModel, ExercisesModel, UserModel
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer


class WorkModelSerializer(DocumentSerializer):
    class Meta:
        model = WorkModel
        fields = '__all__'


class ExercisesModelSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = ExercisesModel
        fields = '__all__'


class UserModelSerializer(DocumentSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
