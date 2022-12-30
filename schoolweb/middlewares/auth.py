from django.http import HttpResponse, HttpResponseRedirect

class AuthMiddleware:
  def __init__(self, get_response):
      self.get_response = get_response
      self.urls = [
        '/login/', '/admin/', '/logout/', '/api/'
      ]
      self.urlsApplications = [
        'user'
      ]
      self.entities = { "professor": "teacher", "estudante": "students", "admin":"admin" }

  def __call__(self, request):
      response = self.get_response(request)

      for url in self.urls:
        pathSplit = request.path.split('/')
        if pathSplit[1].replace('/', '') == url.replace('/', ''): return response
      
      token = request.session.get('access_token')
      type = request.session.get('type')

      path = pathSplit = request.path.split('/')[1].replace('/', '')
      
      if token:
        if type == 'admin' and path == 'school-admin' or path == "":
          return response

        if type == 'user' and path == 'user' or path == "":
          return response

      if token and type == 'admin':
        return HttpResponse('área pessoal de usuários <a href="/school-admin">retornar ao painel admin<a/>')
      if token and type == 'user':
        return HttpResponse('Você não tem permissão <a href="/user">retornar ao painel de usuário<a/>')
      else:
        return HttpResponseRedirect('/login')
  