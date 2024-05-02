from rest_framework.serializers import ModelSerializer

from .models import Chiefs


class CEOSerializer(ModelSerializer):
    class Meta:
        model = Chiefs
        fields = '__all__'
