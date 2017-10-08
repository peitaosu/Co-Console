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

## Settings

There are some settings in `settings.py` may need to be set if you want to have better experience as expected.

```
# IP whitelist for what ip can use this console
CONSOLE_WHITELIST = [
    "127.0.0.1"
]

# change the default current working directory
CONSOLE_CWD = None

# command whitelist for what commands user can use, you need to prepare your environment and add commands into whitelist.
COMMAND_WHITELIST = [
    "dir",
    "ls"
]

# redirect command if need
COMMAND_MAPPING = {
    "ls" : "dir"
}

# add other path into sys.path
APPEND_PATH = []
```
