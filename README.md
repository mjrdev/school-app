## Aplicação Web de Gerenciamento Escolar
##### Case de Processo Seletivo Dev FullStack
### Tecnologias utilizadas:
> Python, Django, SQLite, Docker, Bootstrap, HTML, CSS, JavaScript, JQuery

![admin platform](/docs/admin.jpg)

##### Estrutura do projeto
 * /database  - arquivo do banco de dados
 * /schoolapi - arquivos e módulos da 
    * admin.py - configura entidades para o admin do Django
    * models.py - arquivos e módulos/entidades
    * serialize.py - manipulação de campos
    * views.py - controller da aplicação
 * /schoolweb   - arquivo do banco de dado
    * /middlewares - middlewares da aplicação
    * /template - Frontend da aplicação
      * /user - html da plataforma de usuário
      * /school-admin - html da plataforma de administrador
    * /views - controllers da aplicação
    * models.py - arquivos e módulos/entidades
    * urls.py - arquivo de configuração de rotas
 * /static   - arquivos estáticos


## A aplicação consiste em 2 níveis de usuários:
  * __Admin__: Tem total controle da dos dados da aplicação
    * Acesso em /admin e  /school-admin
  * __User__: Dividido em dois
    * Aluno: Acesso apenas a plataforma de informações /user
    * Professor: Acesso apenas a plataforma de informações /user

![user platform](/docs/user.jpg)

### Entidades da aplicação
  1. Students - Alunos
  1. Teacher - Professores
  1. Courses - Cursos
  1. Registrations - Matriculas
  1. Admin - Super User do Django

### Como rodar:
Com docker
```bash
> git clone https://github.com/mjrdev/school-app.git
> cd school-app
> docker-compose up --build -d
> docker exec -it django bash
> python manage.py createsuperuser --username 'username' --email 'email'
/* informe o username e email do admin, sem aspas. É necessário para primeiro acesso a aplicação */
```
Acesse: http://localhost:8000
### Como rodar sem docker:
Você deve ter o python instalado localmente
```bash
Linux e Mac
$ git clone https://github.com/mjrdev/school-app.git
$ cd school-app
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser --username 'username' --email 'email'
/* informe o username e email do admin, sem aspas. É necessário para primeiro acesso a aplicação */
$ python manage.py runserver
```
Acesse: http://localhost:8000
```bash
Windows (use o powershell)
> git clone https://github.com/mjrdev/school-app.git
> cd school-app
> python -m venv venv
> venv\Scripts\Activate.ps1
> pip install -r requirements.txt
> python manage.py migrate
> python manage.py createsuperuser --username 'username' --email 'email'
/* informe o username e email do admin, sem aspas. É necessário para primeiro acesso a aplicação */
> python manage.py runserver
```
Acesse: http://localhost:8000
