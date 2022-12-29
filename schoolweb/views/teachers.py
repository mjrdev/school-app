from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

class TeacherView:
  def index(request):
    return render(request, './teacher/index.html')