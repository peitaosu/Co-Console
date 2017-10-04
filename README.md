# Co-Console

[![GitHub license](https://img.shields.io/badge/license-New%20BSD-blue.svg)](https://raw.githubusercontent.com/peitaosu/Co-Console/master/LICENSE)

## What is Co-Console ?

Co-Console is a Web-based Console, powered by `django` and `django-console`.

## Setup

Co-Console is a django project, please install Django and required modules before you run the server.

```
pip install Django

# or install from requirements.txt

pip install -r requirements.txt

# python path/to/manage.py runserver 0.0.0.0:{your_port}

python manage.py runserver 0.0.0.0:1234
```

## Commands

Co-Console use whitelist for what commands user can use, so you need to prepare your environment and add commands into whitelist which in settings.