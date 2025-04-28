from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Warehouse(Base):
    __tablename__ = "warehouse_stock"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    warehouse_id: Mapped[str]
    warehouse_code: Mapped[str]
    product: Mapped[str]
    quantity: Mapped[int]