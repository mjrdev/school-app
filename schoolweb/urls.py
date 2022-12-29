from django.urls import path
from schoolweb.views import SchoolWeb

urlpatterns = [
  path('', SchoolWeb.index, name='index'),
  path('login/', SchoolWeb.login, name='login')
]
