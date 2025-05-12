from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm,RegisterForm
from django.contrib import auth
from django.contrib import messages
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Basariyla kayit oldunuz,Giris yapabilirsiniz')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def logout(request):
    auth.logout(request)
    return redirect('home')