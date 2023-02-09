ifneq (,$(wildcard ./.env))
    include .env
    export
endif


# Paths
DIR_APP := $(shell pwd)
DIR_SCRIPTS := $(DIR_APP)/scripts

# -----------------------------------------------
# Variables

RUN := poetry run
PYTHON := poetry run python
WSGI_APPLICATION := tt_web_app.wsgi:application


# ----------------------------------------------

define log
	@tput bold 2>/dev/null || exit 0
	@tput setab 0  2>/dev/null || exit 0
	@tput setaf 4  2>/dev/null || exit 0
	@echo ">>>>>>>>>>>>>>>>    $(1)    "
	@tput sgr0  2>/dev/null || exit 0
endef


# Секция подгтовки
.PHONY: migrations
migrations:
	$(call log, generating migrations)
	$(PYTHON) manage.py makemigrations


.PHONY: migrate
migrate:
	$(call log, applying migrations)
	$(PYTHON) manage.py migrate


PHONY: static
static:
	$(call log, collecting static)
	$(PYTHON) manage.py collectstatic


# Секция запуска


.PHONY: run
run:
	$(PYTHON) manage.py runserver


.PHONY: run-celery
run-celery:
	$(RUN) celery -A tt_web_app worker -B --loglevel=debug


# Секция утилит 


.PHONY: format
format:
	$(call log, reorganizing imports & formatting code)
	$(RUN) black .
	$(RUN) isort .
	

.PHONY: test
test:
	$(call log, running tests)
	$(RUN) pytest


.PHONY: cov
cov:
	$(call log, running tests with coverage)
	$(RUN) pytest --cov


# Остальное
.PHONY: install
install:
	$(call log, installing prod packages)
	poetry install --no-dev


.PHONY: install-dev
install-dev:
	$(call log, installing all packages)
	poetry install
