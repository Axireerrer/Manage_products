from pydantic import BaseModel
from typing import List, Optional


# Cхема для валидации и сериализации Продуктов
class ProductBase(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    cost: Optional[int] = None
    category_id: Optional[int] = None


# Cхема для валидации и сериализации Категорий
class CategoryBase(BaseModel):
    id: int
    name: str
    products: List[ProductBase]

    class Config:
        orm_mode = True

