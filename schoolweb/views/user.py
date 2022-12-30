from django.shortcuts import render
from schoolapi.models import Course, Teacher, Student, Registration

def getUserType(request):
    return request.session.get('access_token').split('-')[0]

def getUserName(request):
    return request.session.get('access_token').split('-')[1]

def getUser(type, name):
  match type:
    case 'student':
      return Student.objects.filter(name=name).get()
    case 'teacher':
      return Teacher.objects.filter(name=name).get()

class UserViews:
  def index(request):
    courses = Course.objects.all()
    type = getUserType(request)
    name = getUserName(request)
    user = getUser(type, name)
    
    return render(request, './user/index.html', { 'courses': courses, 'type': type, 'user': user })

  def courses(request):
    courses = Course.objects.all()
    type = getUserType(request)
    name = getUserName(request)
    user = getUser(type, name)
    return render(request, './user/courses.html', { 'courses': courses, 'type': type, 'user': user })

  def teachers(request):
    teachers = Teacher.objects.all()
    type = getUserType(request)
    name = getUserName(request)
    user = getUser(type, name)
    return render(request, './user/teachers.html', { 'teachers': teachers, 'type': type, 'user': user })

  def profile(request):
    type = getUserType(request)
    name = getUserName(request)
    user = getUser(type, name)

    registration = Registration.objects.all().filter(student_id=user.id)
    countRegistrations = len(registration)
    
    return render(request, './user/profile/index.html', { 'countRegistrations': countRegistrations, 'type': type, 'user': user })

  def profileCourses(request):
    type = getUserType(request)
    name = getUserName(request)
    user = getUser(type, name)
    registration = Registration.objects.all().filter(student_id=user.id)

    return render(request, './user/profile/courses.html', { 'registrations': registration, 'type': type, 'user': user })