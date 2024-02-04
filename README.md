poetry config --local virtualenvs.in-project true
poetry init - n
poetry install
poetry add sqlalchemy
.\.venv\Scripts\Activate 
poetry add alembic
poetry add asyncpg
poetry add psycopg2
poetry add psycopg2-binary
poetry add "fastapi[all]"

alembic init migrations
alembic revision --autogenerate -m 'initial'
