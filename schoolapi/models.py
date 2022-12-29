from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=90)
  email = models.EmailField()
  cpf = models.CharField(max_length=11)
  password = models.CharField(default="12345678", max_length=35)

  def __str__(self):
    return self.name

class Teacher(models.Model):
  name = models.CharField(max_length=90)
  cpf = models.CharField(max_length=11)
  password = models.CharField(default="A12345678", max_length=30)

  def __str__(self):
    return self.name

class Course(models.Model):
  title = models.CharField(max_length=90)
  description = models.TextField()
  # workload = models.IntegerField()
  teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

class StudentOnCourse(models.Model):
  course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
  student_id = models.ForeignKey(Student, on_delete=models.CASCADE)