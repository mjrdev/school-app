from django.contrib import admin
from schoolapi.models import Student, Course

class Students(admin.ModelAdmin):
  list_display = ('id', 'name', 'cpf')
  list_display_links = ('id', 'name')
  search_fields = ('name',)

class Courses(admin.ModelAdmin):
  list_display = ('id', 'title', 'description')
  list_display_links = ('id', 'title')
  search_fields = ('title',)

admin.site.register(Student, Students)
admin.site.register(Course, Courses)
    