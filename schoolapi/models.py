from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=90)
  email = models.EmailField()
  cpf = models.CharField(max_length=11, unique=True)
  password = models.CharField(max_length=35)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name


class Teacher(models.Model):
  name = models.CharField(max_length=90)
  email = models.EmailField()
  cpf = models.CharField(max_length=11)
  password = models.CharField(max_length=35)
  about = models.CharField(max_length=255, null=True)

  def __str__(self):
    return self.name

class Course(models.Model):
  SHIFT = (('noturno', 'noturno'), ('matutino', 'matutino'), ('vespertino', 'vespertino'), ('integral', 'integral'), ('EAD', 'EAD'))
  shift = models.CharField(max_length=15, choices=SHIFT)
  title = models.CharField(max_length=90)
  description = models.TextField()
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')

  def __str__(self):
    return self.title + ' - ' + self.shift

class Registration(models.Model):
  code = models.CharField(max_length=7)
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="registrations")
  course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="registrations")

  def __str__(self):
    return self.code
