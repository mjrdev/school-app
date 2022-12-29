from django.urls import path
from schoolweb.views.auth import Auth
from schoolweb.views.students import StudentView
from schoolweb.views.teachers import TeacherView

urlpatterns = [
  path('login/', Auth.login, name='login'),
  path('logout/', Auth.logout, name='logout'),

  path('student/', StudentView.index, name='student-index'),

  path('teacher/', TeacherView.index, name='teacher-index'),
]
