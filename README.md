## создать все таблицы из tables.py
`from src.workshop.database import engine`

`from src.workshop.tables import Base`

`Base.metadata.create_all(engine)`