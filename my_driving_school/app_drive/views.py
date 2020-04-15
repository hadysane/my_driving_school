from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Profil was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'users/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'users/login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def studentProfile(request):
    return render(request, 'student/account.html')

def instructorProfile(request): 
    return render(request, 'instructor/account.html')