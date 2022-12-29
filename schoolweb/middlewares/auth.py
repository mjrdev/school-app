from django.http import HttpResponse, HttpResponseRedirect

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.urls = [
          '/login/', '/admin/', '/logout/'
        ]
        self.entities = { "professor": "teacher", "estudante": "students", "admin":"admin" }

    def __call__(self, request):
        response = self.get_response(request)

        for url in self.urls:
          pathSplit = request.path.split('/')
          if pathSplit[1].replace('/', '') == url.replace('/', ''): return response
        
        token = request.session.get('access_token')
        print(pathSplit[1].replace('/', ''), token.split('-')[0])
        if token and pathSplit[1].replace('/', '') == token.split('-')[0]:
          return response
        else:
          return HttpResponse('not authorized', status=401)