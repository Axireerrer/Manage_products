from fastapi import APIRouter
from Repositories.categories import CategoryRepository
from typing import List
from schemas.schemas import CategoryBase

router = APIRouter(prefix="/categories", tags=["Categories"])


# API endpoint для получения списка категорий и информации о продуктах в каждой категории
@router.get("", response_model=List[CategoryBase])
async def get_categories():
    categories = await CategoryRepository.read_categories()
    return categories
