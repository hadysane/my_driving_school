from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100,null=False)
    adress = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100, null=False)
    zip_code = zip_code = models.CharField(max_length=5, default="43701", null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10,null=False)
    age = models.DateField()
    nb_hour_lesson = models.CharField(max_length=255,null=True)
    nb_hour_Paid = models.CharField(max_length=255,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.lastname, self.firstname)

  
class Instructor(models.Model):
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100,null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=10,null=False)
    students = models.ManyToManyField(Student)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.lastname, self.firstname)


class RdvDrive(models.Model): 
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = zip_code = models.CharField(max_length=5, default="43701")
    date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    nb_hour = models.CharField(max_length=255, null=True,)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '{} {} | {} {} -- {}'.format(self.instructor.lastname ,self.instructor.firstname,  
        self.student.lastname ,self.student.firstname, self.date)