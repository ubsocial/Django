# API REST com Django REST Framework

## Preparo
1. Instalar Django REST Framework (Necessário Django e pip instalados): pip install djangorestframework

2. Criar projeto Django: django-admin startproject projetoApiRest
	2.1. Dentro do projeto criado, criar app Django: python3 manage.py startapp api
3. Em 'settings.py', em INSTALLED_APPS, informar 'api.apps.AppConfig' e 'rest_framework' como últimos elementos do array
4. Em 'api/models.py', criar model Task (class Task)
5. Em 'projetoApiRest/urls.py', informar rotas (path, informar também include no from)
6. Em 'api/urls.py', informar conteúdo
7. Em 'api/views.py', informar view apiOverview (def apiOverview, informar from adicional também)
8. Executar projeto: python3 manage.py runserver
	8.1. No browser, acessar api (http://127.0.0.1:8000/api/)
