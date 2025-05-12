from django import forms
from .models import Acil_Durum


class AcilDurumForm(forms.ModelForm):
    class Meta:
        model = Acil_Durum
        fields = ['isim', 'soyisim', 'resim', 'telefon', 'adress']
        widgets = {
            'isim': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'soyisim': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'resim': forms.FileInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 100%;'}),
            'adress': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'style': 'width: 100%;'}),
        }
