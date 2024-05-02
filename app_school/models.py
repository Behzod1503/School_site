from django.db import models


# Create your models here.
class Chiefs(models.Model):
    positions = {
        ('1', 'Director'),
        ('2', 'Vice director for academic affairs'),
        ('3', 'Vice director for scientific affairs'),
    }
    ceo_position = models.CharField(max_length=50, verbose_name='Position', choices=positions)
    ceo_fullname = models.CharField(max_length=60, verbose_name='Full name')
    ceo_phone = models.CharField(max_length=15, verbose_name='Phone number', null=True, blank=True)
    ceo_email = models.EmailField(max_length=50, verbose_name='Email', null=True, blank=True)
    days = {
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday')
    }
    ceo_prime_day = models.CharField(max_length=10, verbose_name='Prime days', choices=days)
    ceo_prime_time = models.CharField(max_length=15, verbose_name='Prime time')
    ceo_image = models.ImageField(upload_to='ceo', verbose_name='Image')
    ceo_desc = models.CharField(max_length=300, verbose_name='Description')

    def __str__(self):
        return self.ceo_fullname

    class Meta:
        db_table = 'school_chiefs'
        ordering = ['ceo_position']
