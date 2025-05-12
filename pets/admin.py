from django.contrib import admin
from .models import Hayvan
# Register your models here.
from django.contrib import admin
from .models import Hayvan,hayvan_tur
import csv
from django.http import HttpResponse


def export_hayvan_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="hayvanlar.csv"'
    writer = csv.writer(response)

    # CSV dosyasının başlık satırı
    writer.writerow(['ID', 'İsim', 'Tür', 'Yaş'])

    # Model verilerini yazma
    for hayvan in queryset:
        writer.writerow([hayvan.id, hayvan.ad, hayvan.tur, hayvan.yas,hayvan.cins])

    return response


export_hayvan_csv.short_description = "Seçilen Hayvanları CSV olarak dışa aktar"
class HayvanAdmin(admin.ModelAdmin):
    actions = [export_hayvan_csv]
    list_display = ('ad', 'slug', 'tur', 'cins', 'yas', 'uygun', 'olusturulma_tarihi','guncelleme_tarihi','durum')
    list_filter = ('tur', 'uygun','durum')
    search_fields = ('ad', 'cins', 'aciklama')
    prepopulated_fields = {'slug': ('ad',)}
class TurAdmin(admin.ModelAdmin):
    list_display = ('hayvan_turu','olusturulma_tarihi')
    list_filter=('hayvan_turu',)



admin.site.register(Hayvan,HayvanAdmin)
admin.site.register(hayvan_tur,TurAdmin)
