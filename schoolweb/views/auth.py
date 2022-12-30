from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from schoolapi.models import Student, Teacher
from schoolweb.generate import generate_code

class Auth:
  def login(request):
    type = request.POST.get('type')

    if request.session.get('access_token'): return HttpResponseRedirect('/user')
    if(request.method == 'GET'):
      return render(request, './login.html')

    entities = { "professor": "teacher", "estudante": "student", "admin":"admin" }
    
    cpf = request.POST.get('cpf')
    password = request.POST.get('password')

    # switch para seleção de Model professor e aluno

    user = None
    match type:
      case 'professor':
        user = Teacher.objects.filter(cpf=cpf).first()
      case 'estudante':
        user = Student.objects.filter(cpf=cpf).first()

    if user:
      if user.password == password:
        request.session['access_token'] = entities[type]+"-"+user.name
      else: return render(request, './login.html', { 'error': 'CPF ou senha incorreta' })
    else: return render(request, './login.html', { 'error': 'usuário não encontrado' })

    return HttpResponseRedirect('/user')


  def logout(request):
    del request.session['access_token']
    return HttpResponseRedirect('/login/')