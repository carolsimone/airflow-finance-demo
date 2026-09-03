.PHONY: up down logs run
up:   ; docker compose up -d --build
down: ; docker compose down -v
logs: ; docker compose logs -f scheduler
run:  ; docker compose exec -T scheduler airflow dags trigger finance_daily
