postgres:
	docker run --name postgres15 -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=mysecretpassword -d postgres:15.2-alpine
createdb:
	docker exec -it postgres15 createdb --username=root --owner=root llm-playground
dropdb:
	docker exec -it postgres15 dropdb llm-playground
