manage_py := python ./app/manage.py

run:
	$(manage_py) runserver

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

flake:
	flake8 app/