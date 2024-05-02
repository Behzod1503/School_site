from django.db import models


# Create your models here.
class AboutSchool(models.Model):
    school_name_uz = models.CharField(max_length=255, verbose_name='Maktab nomi')
    school_name_en = models.CharField(max_length=255, verbose_name='School name', blank=True, null=True)
    school_name_ru = models.CharField(max_length=255, verbose_name='Название школы', blank=True, null=True)

    school_logo = models.ImageField(upload_to='school/', blank=True, null=True)

    school_address_uz = models.TextField(verbose_name='Maktab adresi')
    school_address_en = models.TextField(verbose_name='School address', blank=True, null=True)
    school_address_ru = models.TextField(verbose_name='Адрес школы', blank=True, null=True)

    school_email = models.EmailField(verbose_name='Email', blank=True, null=True)
    school_phone = models.CharField(verbose_name='Telefon', blank=True, null=True)
    school_prime_times = models.CharField(max_length=50, verbose_name='Qabul vaqtlari', blank=True, null=True)

    school_location_lat = models.CharField(max_length=15, verbose_name='Latitude', blank=True, null=True)
    school_location_lon = models.CharField(max_length=15, verbose_name='Longitude', blank=True, null=True)

    school_smm_tg = models.CharField(max_length=50, verbose_name='Telegram', blank=True, null=True)
    school_smm_fb = models.CharField(max_length=50, verbose_name='Facebook', blank=True, null=True)
    school_smm_ig = models.CharField(max_length=50, verbose_name='Instagram', blank=True, null=True)
    school_smm_yt = models.CharField(max_length=50, verbose_name='Youtube', blank=True, null=True)

    def __str__(self):
        return self.school_name_uz

    class Meta:
        db_table = 'school_infos'


class Documents(models.Model):
    doc_title_uz = models.CharField(max_length=255, verbose_name='Hujjat nomi')
    doc_title_en = models.CharField(max_length=255, verbose_name='Document title', blank=True, null=True)
    doc_title_ru = models.CharField(max_length=255, verbose_name='Название документа', blank=True, null=True)

    doc_types = {
        ('1', 'Qonun'),
        ('2', 'Qaror'),
        ('3', 'Farmoyish'),
        ('4', 'Buyruq'),
        ('5', 'Farmon'),
    }
    doc_type = models.CharField(max_length=15, choices=doc_types, verbose_name='Toifa/Type')
    org_types = {
        ('1', 'Parlament'),
        ('2', 'Prezident'),
        ('3', 'Vazirlar mahkamasi'),
        ('4', 'Xalq talimi vazirligi'),
        ('5', 'Boshqarma'),
    }
    doc_org = models.CharField(max_length=25, choices=org_types, verbose_name='Tashkilot/Organisation')
    doc_code = models.CharField(max_length=50, verbose_name='№')
    doc_date = models.DateField(verbose_name='Hujjat qabul qilingan vaqt')
    doc_link = models.URLField(max_length=500, verbose_name='Hujjat matni havolasi', blank=True, null=True)

    def __str__(self):
        return self.doc_title_uz[:25]

    class Meta:
        db_table = 'documents'


