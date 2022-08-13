# Makefile

install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 hexlet_pytest
