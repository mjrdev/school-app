from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=90)
  cpf = models.CharField(max_length=11)
  code = models.CharField(max_length=8)
  # created_at = models.DateTimeField(auto_now_add=True)
  # updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Courses(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=1000)

  def __str__(self):
    return self.title
