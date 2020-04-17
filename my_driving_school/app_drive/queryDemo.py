### all Students driving school
students = Student.objects.all()

### all RDVdrives
rdvDrives = RdvDrive.objects.all()

### all instructors
instructors = Instructor.objects.all()

## student toto
## studentUser.student = toto tata
## studentUser.student.age = 18 10 1995
## studentUser.student.nb_hour_lesson
##studentUser.instructor.id = 7
studentUser = User.objects.get(id=7)



## instructor philip iduser
## studentUser.instructor.id = 3
instructorUser = User.objects.get(id=8)




### RDV student toto id user
rdvDriveToto = RdvDrive.objects.get(student_id=7)

### RDV instructor Philip 
rdvDrivePhilip = RdvDrive.objects.get(instructor_id=3)

### display students of instructor
