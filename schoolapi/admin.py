from django.contrib import admin
from schoolapi.models import Student, Course, Teacher, Registration

class Students(admin.ModelAdmin):
  list_display = ('id', 'name', 'cpf')
  list_display_links = ('id', 'name')
  search_fields = ('name',)

class Courses(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'shift')
  list_display_links = ('id', 'title', 'shift',)
  search_fields = ('title',)

class Teachers(admin.ModelAdmin):
  list_display = ('id', 'name', 'cpf')
  list_display_links = ('id', 'name')
  search_fields = ('name',)

class Registrations(admin.ModelAdmin):
  list_display = ('id', 'code', 'course', 'student')
  list_display_links = ('id', 'code', 'course',)
  search_fields = ('id',)

admin.site.register(Student, Students)
admin.site.register(Course, Courses)
admin.site.register(Teacher, Teachers)
admin.site.register(Registration, Registrations)