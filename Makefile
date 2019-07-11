all:
	@echo "Commands:"
	@echo " run-postgres:   start Docker-container with PostgreSQL"
	@echo " remove-postgres:   remove Docker-container with PostgreSQL"
	@echo " run-server:     start django server listening 8040 port"
	@echo " test:           run pytest for django app"
	@echo ""
	@echo "Service commands:"
	@echo " collectstatic"
	@echo " createsuperuser"
	@echo " makemigrations"
	@echo " migrate"

run-postgres:
	docker run -d --rm --name test -e POSTGRES_PASSWORD=123456 -p 32432:5432 -v $(shell pwd)/docker/postgres_data:/var/lib/postgresql/data postgres:11

remove-postgres:
	docker rm -f test

run-server:
	python3 api_server/manage.py runserver 0.0.0.0:8060

test:
	pytest api_server

collectstatic:
	python3 api_server/manage.py collectstatic

makemigrations:
	python3 api_server/manage.py makemigrations

migrate:
	python3 api_server/manage.py migrate

createsuperuser:
	python3 api_server/manage.py createsuperuser
