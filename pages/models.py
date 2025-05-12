from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from pets.models import Hayvan
# Create your models here.
class Acil_Durum(models.Model):
    isim=models.CharField(max_length=100)
    soyisim=models.CharField(max_length=75)
    resim=models.ImageField(upload_to='acil_durum',blank=True, null=True, verbose_name="gorsel")
    telefon = PhoneNumberField()
    adress=models.CharField(max_length=350)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return self.isim + self.soyisim
class Mama(models.Model):
    TUR_CHOICES = [
        ('kopek', 'Köpek'),
        ('kedi', 'Kedi'),
        ('kus', 'Kuş'),
        ('diger', 'Diğer'),
    ]
    hayvan_turu = models.CharField(max_length=20, choices=TUR_CHOICES, verbose_name="Tür")
    mama_adi = models.CharField(max_length=100, verbose_name="İsim")
    aciklama = models.TextField(blank=True, verbose_name="Açıklama")
    fiyat = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat")
    stok = models.PositiveIntegerField(verbose_name="Stok")

    class Meta:
        verbose_name = "Mama"
        verbose_name_plural = "Mamalar"

    def __str__(self):
        return self.mama_adi

