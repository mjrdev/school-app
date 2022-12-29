from django.contrib import admin
from schoolapi.models import Student, Course, Teacher, StudentOnCourse

class Students(admin.ModelAdmin):
  list_display = ('id', 'name', 'cpf')
  list_display_links = ('id', 'name')
  search_fields = ('name',)

class Courses(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'teacher_id')
  list_display_links = ('id', 'title')
  search_fields = ('title',)

class Teachers(admin.ModelAdmin):
  list_display = ('id', 'name', 'cpf')
  list_display_links = ('id', 'name')
  search_fields = ('name',)

class StudentsOnCourses(admin.ModelAdmin):
  list_display = ('id', 'course_id', 'student_id')
  list_display_links = ('id', 'course_id', 'student_id')
  search_fields = ('course_id',)

admin.site.register(Student, Students)
admin.site.register(Course, Courses)
admin.site.register(Teacher, Teachers)
admin.site.register(StudentOnCourse, StudentsOnCourses)
    