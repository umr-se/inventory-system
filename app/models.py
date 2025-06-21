from sqlalchemy import Column, Integer, String
from .db import Base

class InventoryItem(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255), nullable=False)
    quantity = Column(Integer, default=0)
    threshold = Column(Integer, default=10)
