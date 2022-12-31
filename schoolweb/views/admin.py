from django.shortcuts import render
from schoolapi.models import Course, Teacher, Student, Registration
from django.contrib.auth.models import User

class Admin:
  def index(request):

    user = request.session.get('access_token').split('-')[1]
    admin = User.objects.get(username=user)
    return render(request, 'school-admin/index.html', { 'admin': admin })
  def courses(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()

    return render(request,'school-admin/courses.html', {
      'courses': courses, 'teachers': teachers, 'teachers_count': len(teachers), 'courses_count': len(courses)
    })
  def teachers(request):

    teachers = Teacher.objects.all()
    return render(request, 'school-admin/teachers.html', { 'teachers': teachers, 'teachers_count': len(teachers) })
  def students(request):

    students = Student.objects.all()
    return render(request, 'school-admin/students.html', { 'students': students, 'students_count': len(students) })
  def registrations(request):

    registrations = Registration.objects.all()
    courses = Course.objects.all()
    student = Student.objects.all()
    return render(request, 'school-admin/registrations.html', {
      'registrations': registrations, 'courses': courses, 'students': student, 'courses_count': len(courses), 'students_count': len(student), 'registrations_count': len(registrations)
    })

  def profile(request):
    return render(request, 'school-admin/profile.html')