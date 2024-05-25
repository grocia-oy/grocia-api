default:
    just --list

up:
    docker compose up -d

down:
    docker compose down

build:
    docker compose build

exec *args:
    docker compose exec app {{args}}

log *args:
    docker compose logs {{args}} -f

mm *args:
    docker compose exec app alembic revision --autogenerate -m "{{args}}"

migrate:
    docker compose exec app alembic upgrade head

downgrade *args:
    docker compose exec app alembic downgrade {{args}}

test *args:
    docker compose exec app pytest {{args}}
