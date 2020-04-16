from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('profil_student/', views.studentProfile, name="profil_student"),
    path('profil_instructor/', views.instructorProfile, name="profil_instructor"),
    path('dashboard/', views.dashboard, name="dashboard"),

    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout")
]