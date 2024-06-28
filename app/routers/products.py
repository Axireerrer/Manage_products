from fastapi import APIRouter
from Repositories.products import ProductRepository
from typing import Optional, List
from schemas.schemas import ProductBase

router = APIRouter(prefix="/products", tags=["Products"])


# API endpoint для получения списка продуктов и их фильтрации по URL параметрам
@router.get("", response_model=List[ProductBase])
async def get_products(
        name: Optional[str] = None,
        cost: Optional[int] = None,
        ):
    filters_products = ProductBase(name=name, cost=cost)
    products = await ProductRepository.read_products(product_data=filters_products)
    return products


# API endpoint для получения продукта по id
@router.get("/{id}")
async def get_product(id: int):
    product = await ProductRepository.read_product(product_id=id)
    return product


# API endpoint для создания продукта
@router.post("")
async def post_product(product_data: ProductBase):
    new_product = await ProductRepository.create_product(product_data=product_data)
    return new_product


# API endpoint для обновления данных о продукте
@router.put("")
async def put_product(id: int, product_data: ProductBase):
    changed_product = await ProductRepository.update_product(product_data=product_data, product_id=id)
    return changed_product


# API endpoint для удаления продукта
@router.delete("")
async def remove_product(id: int):
    deleted_product = await ProductRepository.delete_product(product_id=id)
    return deleted_product

