from django.shortcuts import render,redirect
from pets.models import Hayvan
from .models import Acil_Durum,Mama
from .forms import AcilDurumForm
from django.contrib import messages
# Create your views here.

#anasayfa
def home(request):
    return render(request,'home.html')

#sahiplenme sayfasi
def sahiplenme(request):
    pets=Hayvan.objects.filter(uygun=True)
    context={
        'pets':pets
    }
    return render(request,'sahiplenme.html',context)

#acilDurum
def acil_durum(request):
    if request.method == 'POST':
        form = AcilDurumForm(request.POST, request.FILES)
        if form.is_valid():
            # Formun verilerini doğrudan kaydet
            form.save()
            messages.success(request, 'HiPet ekipleri sizle iletişime geçip acil duruma müdahale edecektir')
            return redirect('acil_durum')
        else:
            print(form.errors)
    else:
        form = AcilDurumForm()

    context = {
        'form': form
    }
    return render(request, 'acil.html', context)

def mama_sayfasi(request):
    if request.method == 'POST':
        kedi1_checked = request.POST.get('kedi1', False)
        kopek1_checked = request.POST.get('kopek1', False)
        diger_checked = request.POST.get('diger', False)

        # Checkbox'ların durumuna göre işlem yapabilirsiniz
        if kedi1_checked:
            mamalar = Mama.objects.filter(hayvan_turu='kedi')
        elif kopek1_checked:
            mamalar = Mama.objects.filter(hayvan_turu='kopek')
        elif diger_checked:
            mamalar = Mama.objects.filter(hayvan_turu='diger')
        else:
            mamalar = Mama.objects.all()  # Hiçbir şey seçilmediyse tüm mamaları getir
    else:
        mamalar = Mama.objects.all()

    context = {
        'mamalar': mamalar
    }
    return render(request, 'mama.html', context)