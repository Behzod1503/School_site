from rest_framework.viewsets import ModelViewSet

from .models import Chiefs
from .serializers import CEOSerializer


# Create your views here.
class CEOModelViewSet(ModelViewSet):
    serializer_class = CEOSerializer
    queryset = Chiefs.objects.all()
