from django.contrib import admin
from .models import Acil_Durum,Mama
# Register your models here.
class AcilDurumAdmin(admin.ModelAdmin):
    list_display = ('isim', 'soyisim', 'telefon', 'adress', 'olusturulma_tarihi')
    list_filter = ('isim', 'telefon')
    search_fields = ('ad', 'telefon')

@admin.register(Mama)
class MamaAdmin(admin.ModelAdmin):
    list_display = ('hayvan_turu', 'mama_adi', 'fiyat', 'stok')
    list_filter = ('hayvan_turu', 'mama_adi')
    search_fields = ('mama_adi', 'hayvan_turu')

admin.site.register(Acil_Durum,AcilDurumAdmin)
