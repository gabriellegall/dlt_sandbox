start_postgres:
	docker volume create pg_data
	docker run --name local-postgres \
	-e POSTGRES_PASSWORD=azerty \
	-e POSTGRES_DB=sandbox \
	-v pg_data:/var/lib/postgresql/data \
	-p 5432:5432 \
	-d postgres