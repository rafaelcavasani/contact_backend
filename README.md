# contact_backend

API REST para cadastro de contatos telefônicos

# Como Rodar

## * Instalando o ambiente (VirtualEnv)
```
python -m venv venv
pip install -r requirements.txt
```

## * Preparando o banco de dados
```
python manage.py makemigrations
python manage.py migrate
```

## * Subindo o servidor
```
python manage.py runserver
```

# Banco de dados

SQLite

# Deploy na Heroku

https://contacts-be.herokuapp.com/ 
