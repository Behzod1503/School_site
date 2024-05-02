from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import (
    News, Anons, Vacancy,
    Image, PhotoGallery,
    VideoGallery, VideoLinks
)


class NewsSerializer(ModelSerializer):
    news_title = SerializerMethodField()
    news_desc = SerializerMethodField()
    news_text = SerializerMethodField()

    class Meta:
        model = News
        read_only_fields = ('news_views_count',)
        # write_only_fields = ('news_title_uz', 'news_title_ru', 'news_title_ru')
        fields = '__all__'
        extra_kwargs = {
            'news_title_uz': {'write_only': True},
            'news_title_en': {'write_only': True},
            'news_title_ru': {'write_only': True},
            'news_title': {'read_only': True},

            'news_desc_uz': {'write_only': True},
            'news_desc_en': {'write_only': True},
            'news_desc_ru': {'write_only': True},
            'news_desc': {'read_only': True},

            'news_text_uz': {'write_only': True},
            'news_text_en': {'write_only': True},
            'news_text_ru': {'write_only': True},
            'news_text': {'read_only': True}
        }

    def get_news_title(self, obj):
        try:
            match self.context['request'].query_params['lang']:
                case 'uz':
                    return obj.news_title_uz
                case 'en':
                    return obj.news_title_en
                case 'ru':
                    return obj.news_title_ru
                case _:
                    return obj.news_title_uz
        except:
            return obj.news_title_uz

    def get_news_desc(self, obj):
        try:
            match self.context['request'].query_params['lang']:
                case 'uz':
                    return obj.news_desc_uz
                case 'en':
                    return obj.news_desc_en
                case 'ru':
                    return obj.news_desc_ru
                case _:
                    return obj.news_desc_uz
        except:
            return obj.news_desc_uz

    def get_news_text(self, obj):
        try:
            match self.context['request'].query_params['lang']:
                case 'uz':
                    return obj.news_text_uz
                case 'en':
                    return obj.news_text_en
                case 'ru':
                    return obj.news_text_ru
                case _:
                    return obj.news_text_uz
        except:
            return obj.news_text_uz


class AnonsSerializer(ModelSerializer):
    class Meta:
        model = Anons
        fields = '__all__'


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class PhotoGallerySerializer(ModelSerializer):
    gallery_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = PhotoGallery
        read_only_fields = ['gallery_views_count',]
        fields = '__all__'


class VideoLinksSerializer(ModelSerializer):
    class Meta:
        model = VideoLinks
        fields = '__all__'


class VideoGallerySerializer(ModelSerializer):
    gallery_videos = VideoLinksSerializer(many=True, read_only=True)

    class Meta:
        model = VideoGallery
        read_only_fields = ['gallery_views_count',]
        fields = '__all__'
