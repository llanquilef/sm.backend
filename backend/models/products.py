
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric, Enum
from sqlalchemy.dialects.postgresql import UUID
from models.conn_db import Base
import uuid
from utils.timestamps.DateTimeToUTC import get_time_to_utc
from backend.enums.productEnums import UNITS_ENUMS

class ProductBase(Base):
    __tablename__ = "products"
    """ 
    Clase ProductBase: Define clase base de Products
    ProductBase Class: Define base class of products
    """
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(250), max_length=400, nullable=True)
    sku = Column(String(12), default=0, nullable=False)
    stockQuantity = Column(Integer, default=0, nullable=False)
    unit = Column(Enum, default=UNITS_ENUMS[0], nullable=False)
    buyPrice = Column(Numeric, default=0.0, nullable=False)
    salePrice = Column(Numeric, default=0.0, nullable=False)
    minStockLevel = Column(Integer, default=0, nullable=True)
    profitMargin = Column(Numeric, default=0.0, nullable=True)
    status = Column(Boolean, default=False, nullable=False)
    
class ProductCreate(ProductBase):
    super.__init__()
    createdAt = Column(DateTime(timezone=True))
    #featuresDict: dict = Field(featuresJSON.items)
    #featuresList: list = Field(featuresList) 

class ProductUpdate(ProductBase):
    super.__init__()
    updatedAt = Column(DateTime(timezone=True))
    
class ProductDelete(ProductBase):
    """ Clase ProductDelete:  """
    super.__init__()
    deletedAt = Column(DateTime(timezone=True))

