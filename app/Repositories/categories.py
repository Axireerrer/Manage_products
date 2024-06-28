from databases.models import Category
from databases.db_core import async_session
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from typing import List
from schemas.schemas import CategoryBase


# Реализация CRUD логики для модели Категории
class CategoryRepository:

    # Получить все категории
    @classmethod
    async def read_categories(cls) -> List[CategoryBase]:
        async with async_session() as session:
            query = select(Category).options(joinedload(Category.products))
            result = await session.execute(query)
            categories = result.unique().scalars().all()
            return categories
