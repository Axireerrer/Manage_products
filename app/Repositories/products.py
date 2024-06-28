from databases.models import Product
from databases.db_core import async_session
from sqlalchemy import select
from fastapi.exceptions import HTTPException
from schemas.schemas import *


# Реализация CRUD логики для модели Продуктов
class ProductRepository:

    # Получить все продукты или продукты по заданным URL параметрам
    @classmethod
    async def read_products(
            cls,
            product_data: ProductBase
    ):
        async with async_session() as session:

            if product_data.name:
                query = select(Product).filter(product_data.name == Product.name)

            elif product_data.cost:
                query = select(Product).filter(product_data.cost == Product.cost)

            else:
                query = select(Product)

            result = await session.execute(query)
            products = result.scalars().all()
            return products

    # Получить продукт по идентификатору
    @classmethod
    async def read_product(cls, product_id: int):
        async with async_session() as session:
            query = select(Product).where(product_id == Product.id)
            result = await session.execute(query)
            product = result.scalar_one_or_none()

            if product is None:
                raise HTTPException(status_code=404, detail="Product Not Found")

            return product

    # Создать продукт
    @classmethod
    async def create_product(cls, product_data: ProductBase):
        async with async_session() as session:
            product_dict = product_data.model_dump()
            new_product = Product(**product_dict)
            session.add(new_product)
            await session.flush()
            await session.commit()
            return new_product

    # Обновить данные о продукте
    @classmethod
    async def update_product(cls, product_data: ProductBase, product_id: int):
        async with async_session() as session:
            query = select(Product).where(product_id == Product.id)
            result = await session.execute(query)
            product = result.scalar_one_or_none()

            if product is None:
                raise HTTPException(status_code=404, detail="Product Not Found")

            product_data = product_data.model_dump(exclude_unset=True)

            for key, value in product_data.items():
                setattr(product, key, value)

            await session.commit()
            await session.refresh(product)
            return product

    # Удалить продукт
    @classmethod
    async def delete_product(cls, product_id: int):
        async with async_session() as session:
            query = select(Product).where(product_id == Product.id)
            result = await session.execute(query)
            product = result.scalar_one_or_none()

            if product is None:
                raise HTTPException(status_code=404, detail="Product Not Found")

            await session.delete(product)
            await session.flush()
            await session.commit()
            return product

