from datetime import datetime

from src.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column



class Movement(Base):
    __tablename__ = "movement"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    movement_id: Mapped[str]
    event: Mapped[str]
    source: Mapped[str]
    warehouse_id: Mapped[str]
    timestamp: Mapped[datetime]
    product_id: Mapped[str]
    quantity: Mapped[int]