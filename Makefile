SHELL := /bin/bash
CHDIR_SHELL := $(SHELL)

##### v3.0.0
##### SETTINGS
NAME = PROJECTNAME
PORT = 8000
SOURCE = live
DB = psql
# psql or mysql

##### VARIABLES
ENV = env
VENV = $(ENV)/bin/activate
PTYHON = $(ENV)/bin/python
PIP = . $(VENV); $(ENV)/bin/pip
PROJECT_DIR = ./src
FAB = $(ENV)/bin/fab
MANAGE = @DJANGO_SETTINGS_MODULE=settings_local $(PTYHON) src/local
BRANCH=`git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'`


##### CORE COMMANDS
##### You need to be within the repository for excecution
all:
	##### automatically run the project with all requirements
	make -j4 server tasks css

install:
ifneq ("$(wildcard $(PROJECT_DIR)/settings_local.py)","")
	##### setup has already been excecuted, please use "make update" or remove "settings_local.py";
	exit 1
endif
	mkdir -p tmp
	##### pull from git
	-git pull origin $(BRANCH)
	##### create virtualenv
	test -d $(VENV) || virtualenv $(ENV) --prompt="(`basename \`pwd\``)"
	##### create local settings file
	cp -f $(PROJECT_DIR)/settings_local.py-example $(PROJECT_DIR)/settings_local.py
	##### install requirements
	$(PIP) install -r requirements.txt --upgrade
	npm install
	##### create database
ifeq '$(DB)' 'psql'
	-psql -U postgres -c 'DROP DATABASE $(NAME)_local;'
	psql -U postgres -c 'CREATE DATABASE $(NAME)_local;'
else ifeq '$(DB)' 'mysql'
	-mysql -u root -e 'DROP DATABASE $(NAME)_local;'
	mysql -u root -e 'CREATE DATABASE $(NAME)_local;'
endif
	##### insert database data
	export LANG="en_US.UTF-8"  # fixing django bug #16017
	$(MANAGE) syncdb --all
	$(MANAGE) migrate --fake
	##### finished

update:
	##### pull from git
	-git pull origin $(BRANCH)
	##### update requirements
ifdef UPGRADE
	$(PIP) install -r requirements.txt --upgrade
else
	$(PIP) install -r requirements.txt
endif
	npm update
	##### update database data
	$(MANAGE) syncdb
	$(MANAGE) migrate
	##### finished

run:
	make -j4 server tasks

tests:
	##### todo


##### HELPER COMMANDS
server:
	$(MANAGE) runserver 0.0.0.0:$(PORT)

tasks:
	. $(VENV); gulp

css:
	compass watch private --sourcemap
