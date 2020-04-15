from django.contrib import admin
from .models import Student, Instructor, RdvDrive

# Register your models here.
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(RdvDrive)