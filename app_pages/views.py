from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .serializers import SchoolInfoSerializer, DocumentsSerializer
from .models import AboutSchool, Documents
from .filters import DocSearchFilterBackend


class SchoolInfoViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolInfoSerializer
    queryset = AboutSchool.objects.all()


class DocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentsSerializer
    queryset = Documents.objects.all()


class DocumentsSearchAPIView(ListAPIView):
    filter_backends = (DocSearchFilterBackend,)
    serializer_class = DocumentsSerializer

    def get_queryset(self):
        try:
            key_word = self.kwargs['title']
            # key_word = self.request.GET['value'] # query paramdan olish
            queryset = Documents.objects.filter(doc_title_uz__icontains=key_word) | Documents.objects.filter(doc_title_ru__icontains=key_word) | Documents.objects.filter(doc_title_en__icontains=key_word)
        except:
            queryset = Documents.objects.none()
        return queryset