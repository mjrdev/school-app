from django.db import models

import string
import random

def generate_code(stringSize, NumberSize):
  return ''.join(random.choice(string.ascii_uppercase) for _ in range(stringSize)) + ''.join(random.choice(string.digits) for _ in range(NumberSize))

class Student(models.Model):
  name = models.CharField(max_length=90)
  email = models.EmailField()
  cpf = models.CharField(max_length=11, unique=True)
  password = models.CharField(default="12345678", max_length=35)

  def __str__(self):
    return self.name

class Teacher(models.Model):
  name = models.CharField(max_length=90)
  email = models.EmailField()
  cpf = models.CharField(max_length=11)
  password = models.CharField(default="12345678", max_length=35)

  def __str__(self):
    return self.name

class Course(models.Model):
  SHIFT = (('noturno', 'noturno'), ('matutino', 'matutino'), ('vespertino', 'vespertino'), ('integral', 'integral'))
  shift = models.CharField(max_length=15, choices=SHIFT)
  title = models.CharField(max_length=90)
  description = models.TextField()
  # workload = models.IntegerField()
  def __str__(self):
    return self.title + ' - ' + self.shift

class Registration(models.Model):
  code = models.CharField(max_length=9, default=generate_code(3, 6))
  course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
  student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

  def __str__(self):
    return self.code
