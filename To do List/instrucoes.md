# Aplicação To do list com Django:

## Preparo:
1- Instalar pip: sudo apt install python3-pip
2- Instalar Django: pip install django
3- Criar projeto: django-admin startproject nomePastaProjeto (Informado, nesse caso, 'todo')
4- Criar migrations: python3 manage.py migrate
5- Criar usuário: python3 manage.py createsuperuser (Informar dados)
6- Executar projeto: python3 manage.py runserver (Acessar em http://127.0.0.1:8000)
    6.1- Pode-se acessar painel admin com credenciais informadas acima (http://127.0.0.1:8000/admin)
7- Iniciar projeto: python3 manage.py startapp nomeApp (Informado, nesse caso, 'tasks')

8- Em todo/settings.py, informar, em INSTALLED_APPS, o nome do app como último item da lista
9- Em tasks/views.py, informar def index (Informar 'from HttpResponse' também)
10- Em tasks, criar arquivo 'urls.py', criando rota do views.index
11- Em todo/urls.py, incluir 'include' no from django.urls e complementar rota admin.site.urls
12- Testar funcionamento no browser (runserver - Deverá mostrar 'Hello world' na tela)

13- Em tasks, criar pasta 'templates' com subpasta 'tasks'
14- Dentro da pasta acima, criar arquivo 'list.html'
16- Em tasks/views.py, informar rota index
    16.1- Recarregar browser para conferir se rota está funcionando (Irá para list.html)

17- Em tasks/models.py, criar model Task (class Task)
18- Montar migrations (Criar model 'task'): python3 manage.py makemigrations
19- Criar migrations: python3 manage.py migrate
20- Executar projeto: python3 manage.py runserver
21- Em tasks/admin.py, informar 'from .models' e 'admin.site.register'
    21.1- No browser, acessar painel admin (http://127.0.0.1:8000/admin), mostrará novo grupo 'Tasks'
    21.2- Acessar e, após, clicar em 'add task':
        21.2.1- Title: Projeto de ToDo UB Social (Clicar em Save)
        21.2.2- Title: Projeto de ToDo2 UB Social (Clicar em Save)

22- Em tasks/views.py, informar 'from .models' e aprimorar view index
23- Em tasks/templates/list.html, preencher template
23.1- No browser, recarregar index(http://127.0.0.1:8000) e verificar se lista de tasks adicionadas no admin serão mostradas

24- Em tasks, criar novo arquivo 'forms.py' (Será a model TaskForm)
24.1- Em tasks/views.py, incluir 'from .forms'
25- Em tasks/templates/list.html
25.1- No browser, recarregar index e verificar se aparece form de criação de task

26- Em tasks/views.py, incluir if (Incluir 'redirect' no from)
27- No Browser, testar inserções de tasks

PAROU EM 22:00min