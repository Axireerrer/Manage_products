import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from databases.db_core import create_tables, drop_tables
from routers import categories, products


# Создание таблиц в бд и удаление по завершению работы программы
@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(
    title="Manage_products",
    lifespan=lifespan
)

# Подключение роутеров к приложению
app.include_router(products.router)
app.include_router(categories.router)


# Запуск приложения
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)


