from django.urls import path
from schoolweb.views.auth import Auth
from schoolweb.views.user import UserViews
from django.http import HttpResponseRedirect

def redirect(request):
  token = request.session.get('access_token')
  if token:
    return HttpResponseRedirect('/user')
  else:
    return HttpResponseRedirect('/login')

urlpatterns = [
  # path('', redirect),
  path('login/', Auth.login, name='login'),
  path('logout/', Auth.logout, name='logout'),

  path('user/', UserViews.index, name='user-index'),
  path('user/courses/', UserViews.courses, name='user-courses'),
  path('user/teachers/', UserViews.teachers, name='user-courses'),
  path('user/profile', UserViews.profile, name='user-profile'),
  path('user/profile/my-courses', UserViews.profileCourses, name='my-courses'),
]
