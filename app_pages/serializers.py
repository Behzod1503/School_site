from rest_framework.serializers import ModelSerializer

from .models import AboutSchool, Documents


class SchoolInfoSerializer(ModelSerializer):
    class Meta:
        model = AboutSchool
        fields = '__all__'


class DocumentsSerializer(ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'
