from main.models import WorkModel, ExercisesModel, UserModel, BitModel
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


class BitModelSerializer(DocumentSerializer):
    class Meta:
        model = BitModel
        fields = '__all__'