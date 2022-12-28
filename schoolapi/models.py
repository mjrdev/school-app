from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=90)
  cpf = models.CharField(max_length=15)

  def __str__(self):
    return self.name

class Course(models.Model):
  title = models.CharField(max_length=90)
  description = models.TextField()
  

  def __str__(self):
    return self.title

