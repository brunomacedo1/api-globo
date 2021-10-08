<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-rotas">Rotas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>


<br>

## ✨ Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Django](https://www.djangoproject.com/)
- [Django Rest FrameWork](https://www.django-rest-framework.org/)
- [Django Rest Auth](https://django-rest-auth.readthedocs.io/en/latest/) 
- [Pipenv](https://pipenv.pypa.io/en/latest/)

## 💻 Projeto

Api criada para o desafio da globo.
A api tem o objetivo de implmentar Cards esportivos que seram consumidos por uma interface(front-end).
Dentre as funcionalidades da api está a possibilidade de criar, editar, deletar, listar, e listar com filtros Cards, que são insigths esportivos.


## 🚀 Como executar

- Clone o repositório
- Instale o pipenv shell como usuário ( pip install --user pipenv)
- É necessário o python 3.7.x
- Após instalar o pipenvshell, use o comando ' pipenvshell ' para criar uma virtualenv.
- Após criar e ativar a virtualenv, rode o comando pipenv sync, para baixar as dependências da aplicação.
- É necessario também gerar as migrations para a aplicação funcionar. Rode o comando ' python manage.py makemigrations '
  e em seguida execute o comando ' python manage.py migrate '.
- E finalmente para iniciar a aplicação execute o comando, ' python manage.py runserver '.

## Rotas
- http://localhost:8000/admin -> Acesso ao painel do djangoAdmin. É necessário utilizar o comando ' python manage.py createsuperuser '
  para ter acesso a esse painel
- http://localhost:8000/rest-auth/registration/ -> Rota do tipo POST, para registro de usuário.
- http://localhost:8000/rest-auth/login/ -> Rota do tipo POST, para login.
- http://localhost:8000/rest-auth/logout/ -> Rota do tipo POST, para logout.
- http://localhost:8000/api/cards/ -> Rota do tipo GET onde é listada todos os cards da aplicação. E POST para criar um card
- http://localhost:8000/api/cards/id/ -> Rota GET, PUT, DELETE para o card da aplicação.
- http://localhost:8000/api/cards/categoria/ -> Rota para listar o card a partir do filtro de categoria.

