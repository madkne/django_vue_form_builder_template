# Django, Vue.js, Form builder Template Project

This project template creates a Django 3+ project with a base set of applications

## Features

- Django 3+
- mySQL DB
- using vue.js on html templates
- using DAT


## Usage
Create a Django project:

```bash
mkdir my-website.com
cd my-website.com
django-admin.py startproject mywebsite . -e py,rst,example,gitignore,ini,min --template=https://github.com/madkne/django_vue_form_builder_template/archive/master.zip
```

# {{ project_name|title }} Project

## About
Describe your project here.

## Prerequisites
- Python >= 3.6
- pip
- virtualenv (virtualenvwrapper is recommended)

## Deployment of this project is following:

- python3 -m venv venv
- source ./venv/bin/activate
- venv\Scripts\activate (in windows)
- export DJANGO_SETTINGS_MODULE={{project_name}}.settings.development
- sudo apt-get install build-essential python3-dev
- sudo apt-get install default-libmysqlclient-dev (for connecting to mysql)
- pip3 install -r requirements.txt
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver
- also read [Frontend README](./frontend/README.md) file

## License

Describe project license here.
