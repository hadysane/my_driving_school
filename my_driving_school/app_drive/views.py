from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users

def home(request):
    return render(request, 'index.html')

@unauthenticated_user
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

@unauthenticated_user
def loginPage(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request,'Username OR password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request) 
    return redirect('login')
@login_required(login_url='login')


def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def studentProfile(request):
    return render(request, 'student/account.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Instructor'])
def instructorProfile(request): 
    return render(request, 'instructor/account.html')
