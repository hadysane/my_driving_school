from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = zip_code = models.CharField(max_length=5, default="43701")
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    age = models.DateField()

  
class Instructor(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    students = models.ManyToManyField(Student)


class RdvDrive(models.Model): 
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = zip_code = models.CharField(max_length=5, default="43701")
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
