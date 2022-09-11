from fastapi import FastAPI

from .api import router

tags_metadata = [
    {
        'name': 'Auth',
        'description': 'Авторизация и регистрация',
    },
    {
        'name': 'Operations',
        'description': 'Создание, редактирование, удаление и просмотр операций',
    },
    {
        'name': 'Reports',
        'description': 'Импорт и экспорт CSV-отчетов',
    },
]

app = FastAPI(
    title='Workshop',
    description='Сервис учета личных доходов и расходов',
    version='1.0.0',
    openapi_tags=tags_metadata
)
app.include_router(router)
