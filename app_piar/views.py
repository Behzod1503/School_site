import datetime

import jwt
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import (
    News, Anons, Vacancy,
    Image, PhotoGallery,
    VideoLinks, VideoGallery
)
from .serializers import(
    NewsSerializer, AnonsSerializer, VacancySerializer,
    ImageSerializer, PhotoGallerySerializer,
    VideoLinksSerializer, VideoGallerySerializer,
)


class NewsModelViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    
    def create(self, request, *args, **kwargs):
        try:
            token = self.request.META['HTTP_TOKEN']
        except:
            raise AuthenticationFailed('Send token, please')

        if not token:
            raise AuthenticationFailed('Invalid token, login again, please')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired, login again, please')
        except:
            raise AuthenticationFailed('Invalid token, login again, please')

        user = get_user_model().objects.filter(username=payload['username']).first()
        request.data['news_author'] = user.id

        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        try:
            counter = News.objects.filter(pk=self.kwargs['pk']).values_list('news_views_count').first()[0]
            # print(counter)
            News.objects.filter(pk=self.kwargs['pk']).update(news_views_count=counter+1)
        except:
            pass
        return super().retrieve(request, *args, **kwargs)


class AnonsModelViewSet(ModelViewSet):
    serializer_class = AnonsSerializer
    queryset = Anons.objects.all()


class VacancyModelViewSet(ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Vacancy.objects.filter(vacancy_status=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PhotoGalleryModelViewSet(ModelViewSet):
    serializer_class = PhotoGallerySerializer
    queryset = PhotoGallery.objects.all()


class VideoGalleryModelViewSet(ModelViewSet):
    serializer_class = VideoGallerySerializer
    queryset = VideoGallery.objects.all()