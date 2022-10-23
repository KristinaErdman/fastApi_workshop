## создать все таблицы из tables.py
`from src.workshop.database import engine`

`from src.workshop.tables import Base`

`Base.metadata.create_all(engine)`

## сгенерировать jwt_secret
`from secrets import token_urlsafe`

`token_urlsafe()`

или

`openssl rand -hex 32`


## запуск
`cd src`

`uvicorn workshop.__main__:app --reload`

## работа с alembic
`alembic init migrations`

`alembic revision --autogenerate -m "name of migration"` - создать миграцию

`alembic upgrade head` - применить миграции