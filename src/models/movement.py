from datetime import datetime

from sqlalchemy import ForeignKey
from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.warehouse import Warehouse


class Movement(Base):
    __tablename__ = "movement"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    movement_id: Mapped[str]
    event: Mapped[str]
    source: Mapped[str]
    warehouse_id: Mapped[int] = mapped_column(ForeignKey("warehouse_stock.id"))
    warehouse: Mapped["Warehouse"] = relationship("Warehouse", back_populates="movements")
    timestamp: Mapped[datetime]
    product_id: Mapped[str]
    quantity: Mapped[int]