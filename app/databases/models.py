from databases.db_core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


# Модель Продукты
class Product(Base):
    __tablename__ = "Products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    cost: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey("Categories.id"))

    category: Mapped["Category"] = relationship("Category", back_populates="products")

    def __repr__(self):
        return (
            f"Model_Product:\n"
            f"name: {self.name}\n"
            f"description: {self.description}\n"
            f"cost: {self.cost}"
            f"category: {self.category}"
        )

# Модель Категории
class Category(Base):
    __tablename__ = "Categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    products: Mapped[list["Product"]] = relationship("Product")

    def __repr__(self):
        return (
            f"Model_Category:\n"
            f"name: {self.name}\n"
        )
