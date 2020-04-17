from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users
from app_drive.models import *

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
            return redirect('home')
        else:
            messages.info(request,'Username OR password is incorrect')
    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request) 
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Student'])
def studentProfile(request):
    current_user =request.user.id

    user = User.objects.get(id=current_user)
    studentId= user.student.id 
    # instructor = user.instructor.id 
    UserRdv = RdvDrive.objects.filter(student_id=studentId)

    return render(request, 'student/account.html',{'user':user,'userRdv': UserRdv})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Instructor'])

def instructorProfile(request): 
    current_user =request.user.id
    user = User.objects.get(id=current_user)
    students = user.instructor.students.all() 
    return render(request, 'instructor/account.html',{'user': user, 'students': students})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Instructor'])

def dashboard(request):
    current_user =request.user.id

    user = User.objects.get(id=current_user)
    instructorId = user.instructor.id 
    UserRdv = RdvDrive.objects.filter(instructor_id=instructorId) 

    return render(request, 'dashboard.html',{'user':user,'userRdv': UserRdv})