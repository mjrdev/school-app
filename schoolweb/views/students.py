from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

class StudentView:
  def index(request):
    return render(request, './student/index.html')