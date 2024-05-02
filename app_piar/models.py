from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=300, blank=True, null=True)
    news_title_uz = models.CharField(max_length=300, verbose_name='Yangilik sarlavhasi', unique=True)
    news_title_en = models.CharField(max_length=300, verbose_name='News title', unique=True)
    news_title_ru = models.CharField(max_length=300, verbose_name='Заголовок новости', unique=True)

    news_image = models.ImageField(upload_to='images/news', verbose_name='Image', null=True, blank=True)

    news_desc = models.CharField(max_length=500, blank=True, null=True)
    news_desc_uz = models.CharField(max_length=500, verbose_name='Yangilik qisqacha tavsifi')
    news_desc_en = models.CharField(max_length=500, verbose_name='News description', null=True, blank=True)
    news_desc_ru = models.CharField(max_length=500, verbose_name='Описание новости', null=True, blank=True)

    news_text = models.TextField(blank=True, null=True)
    news_text_uz = models.TextField(verbose_name='Yangilik to‘liq matni')
    news_text_en = models.TextField(verbose_name='News full text', null=True, blank=True)
    news_text_ru = models.TextField(verbose_name='Текст новости', null=True, blank=True)

    news_datetime = models.DateTimeField(auto_now_add=True)
    news_views_count = models.IntegerField(verbose_name='Ko‘rishlar soni', default=0)
    news_source = models.URLField(verbose_name='Manba (agar mavjud bo‘lsa)', null=True, blank=True)

    news_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=5)

    class Meta:
        db_table = 'pr_news'
        ordering = ('-news_datetime', )

    def __str__(self):
        return f"{self.id}. {self.news_title_uz}"


class Anons(models.Model):
    anons_title_uz = models.CharField(max_length=300, verbose_name='E\'lon sarlavhasi')
    anons_title_en = models.CharField(max_length=300, verbose_name='Announcement title')
    anons_title_ru = models.CharField(max_length=300, verbose_name='Заголовок объявление')

    anons_desc_uz = models.CharField(max_length=500, verbose_name='E\'lon qisqacha tavsifi')
    anons_desc_en = models.CharField(max_length=500, verbose_name='Announcement description', null=True, blank=True)
    anons_desc_ru = models.CharField(max_length=500, verbose_name='Описание объявление', null=True, blank=True)

    anons_datetime = models.DateTimeField(auto_now_add=True)
    anons_deadline = models.DateTimeField()

    class Meta:
        db_table = 'pr_anons'
        ordering = ('-anons_datetime', )

    def __str__(self):
        return f"{self.id}. {self.anons_title_uz}"


class Image(models.Model):
    image = models.ImageField(upload_to='images/gallery')

    def __str__(self):
        return self.image

    class Meta:
        db_table = 'gallery_images'


class PhotoGallery(models.Model):
    gallery_title_uz = models.CharField(max_length=255, verbose_name='Fotogalereya sarlavhasi')
    gallery_title_en = models.CharField(max_length=255, verbose_name='Title photogallery')
    gallery_title_ru = models.CharField(max_length=255, verbose_name='Названия фотогалерея')

    gallery_desc_uz = models.CharField(max_length=500, verbose_name='Fotogalereya qisqacha tavsifi')
    gallery_desc_en = models.CharField(max_length=500, verbose_name='Photogallery description', null=True, blank=True)
    gallery_desc_ru = models.CharField(max_length=500, verbose_name='Описание фотогалерея', null=True, blank=True)

    gallery_datetime = models.DateTimeField(auto_now_add=True)
    gallery_views_count = models.IntegerField(verbose_name='Ko‘rishlar soni', default=0)
    gallery_images = models.ManyToManyField(Image)

    class Meta:
        db_table = 'pr_photogallery'
        ordering = ('-gallery_datetime', )


class Vacancy(models.Model):
    vacancy_name_uz = models.CharField(max_length=100, verbose_name='Vakansiya nomi')
    vacancy_name_en = models.CharField(max_length=100, verbose_name='Vacancy name')
    vacancy_name_ru = models.CharField(max_length=100, verbose_name='Названия ваканcия')

    vacancy_desc_uz = models.CharField(max_length=500, verbose_name='Vakansiya qisqacha tavsifi')
    vacancy_desc_en = models.CharField(max_length=500, verbose_name='Vacancy description', null=True, blank=True)
    vacancy_desc_ru = models.CharField(max_length=500, verbose_name='Описание вакансия', null=True, blank=True)

    vacancy_text_uz = models.TextField(verbose_name='Vakansiya to‘liq tavsifi')
    vacancy_text_en = models.TextField(verbose_name='Vacancy full text', null=True, blank=True)
    vacancy_text_ru = models.TextField(verbose_name='Польное описания вакансия', null=True, blank=True)

    vacancy_datetime = models.DateTimeField(auto_now_add=True)
    vacancy_views_count = models.IntegerField(verbose_name='Ko‘rishlar soni', default=0)
    vacancy_status = models.BooleanField(verbose_name='Vakansiya holati', default=True)

    class Meta:
        db_table = 'pr_vacancies'
        ordering = ('-vacancy_datetime', )

    def __str__(self):
        return f"{self.id}. {self.vacancy_name_uz}"


class VideoLinks(models.Model):
    video = models.URLField()

    def __str__(self):
        return self.video

    class Meta:
        db_table = 'gallery_videos_links'


class VideoGallery(models.Model):
    gallery_title_uz = models.CharField(max_length=255, verbose_name='Videogalereya sarlavhasi')
    gallery_title_en = models.CharField(max_length=255, verbose_name='Title videogallery')
    gallery_title_ru = models.CharField(max_length=255, verbose_name='Названия видеогалерея')

    gallery_desc_uz = models.CharField(max_length=500, verbose_name='Videogalereya qisqacha tavsifi')
    gallery_desc_en = models.CharField(max_length=500, verbose_name='Videogallery description', null=True, blank=True)
    gallery_desc_ru = models.CharField(max_length=500, verbose_name='Описание видеогалерея', null=True, blank=True)

    gallery_datetime = models.DateTimeField(auto_now_add=True)
    gallery_views_count = models.IntegerField(verbose_name='Ko‘rishlar soni', default=0)
    gallery_videos = models.ManyToManyField(VideoLinks)

    class Meta:
        db_table = 'pr_videogallery'
        ordering = ('-gallery_datetime', )
