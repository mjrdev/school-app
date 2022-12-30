## Aplicação Web de Gerenciamento Escolar
##### Case de Processo Seletivo Dev FullStack
#### Tecnologias utilizadas:
> Python, Django, SQLite, HTML, CSS e JavaScript

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


#### A aplicação consiste em 2 níveis de usuários:
  * __Admin__: Tem total controle da dos dados da aplicação
  * __User__: Dividido em dois
    * Aluno: 
