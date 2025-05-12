from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify


class hayvan_tur(models.Model):
    hayvan_turu=models.CharField(max_length=55,unique=True,blank=True)
    olusturulma_tarihi=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.hayvan_turu

    class Meta:
        verbose_name = "Hayvan_tur"
        verbose_name_plural = "Hayvan_tur"

class Hayvan(models.Model):
    DURUM_CHOICES = [
        ('Gecici Sahiplendirme', 'Geçici Sahiplendirme'),
        ('Barindirma', 'Barındırma '),
        ('Sahiplendirme', 'Sahiplendirme'),
        ('diger', 'Diğer'),
    ]

    ad = models.CharField(max_length=100, verbose_name="Ad")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="Slug")
    tur = models.ForeignKey(hayvan_tur,on_delete=models.CASCADE)
    cins = models.CharField(max_length=100, blank=True, verbose_name="Cins")
    yas = models.PositiveIntegerField(verbose_name="Yaş")
    aciklama = models.TextField(blank=True, verbose_name="Açıklama")
    resim = models.ImageField(upload_to='hayvan_resimleri/', blank=True, null=True, verbose_name="Resim")
    uygun = models.BooleanField(default=False, verbose_name="Uygun")
    adres=models.CharField(max_length=150,blank=True)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    durum=models.CharField(max_length=150,choices=DURUM_CHOICES,verbose_name='Durum')
    guncelleme_tarihi=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.ad

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ad)
        super(Hayvan, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Hayvan"
        verbose_name_plural = "Hayvanlar"