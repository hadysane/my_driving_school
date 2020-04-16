from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    student = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student",
        null=True,
    )
    age = models.DateField()
    nb_hour_lesson = models.CharField(max_length=255,null=True)
    nb_hour_Paid = models.CharField(max_length=255,null=True)

    def __str__(self):
        return '{} {}'.format(self.student.first_name,self.student.last_name )

  
class Instructor(models.Model):
    instructor = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="instructor",
        null=True
    )
    students = models.ManyToManyField(Student)
   
    def __str__(self):
        return '{} {}'.format(self.instructor.first_name,self.instructor.last_name)


class RdvDrive(models.Model): 
    place = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    nb_hour = models.CharField(max_length=255, null=True,)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '{} {} | {} {}'.format(self.instructor.instructor.first_name,self.instructor.instructor.last_name, self.student.student.first_name,self.student.student.last_name)