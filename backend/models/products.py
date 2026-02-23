import uuid
from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.dialects.postgresql import UUID
from models.base import Base
from utils.timestamps.DateTimeToUTC import get_time_to_utc
from models.company import CompanyBase
from models.supplier import SupplierBase

class ProductBase(Base):
    """ Clase ProductBase: Define clase base de Products
        ProductBase Class: Define base class of products
    """
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(400), nullable=True)
    
# JSON NO A LA BD POR FAVOR 
#featuresJSON = {
#    'Control Stock Inventario': 0,
#    'Boletas y Facturas Electronicas': 1,
#    'Punto de Venta POS': 2,
#    'Contactos': 4,
#    'Gestion Proveedores': 5,
#    'Notas Ventas': 6, 
#    'Ordenes de Compra': 7,
#    'Impuestos Adicionales': 8, 
#    'Facturas de Compra': 9
#    }

#featuresList = [
#    'Boletas y Facturas Electronicas',
#    'Control Stock Inventario' 
#    'Punto de Venta POS'
#    'Contactos'
#    'Gestion de Proveedores'
#    'Notas de Venta' 
#]
class ProductFK(ProductBase): 
    super.__init__()
    companyId: uuid.UUID = Field(foreign_key=CompanyBase.id) 
    supplierId: uuid.UUID = Field(foreign_key=SupplierBase.id)

class ProductCreate(ProductBase):
    super.__init__()
    createdAt: datetime = Field(default_factory=get_time_to_utc)
    #featuresDict: dict = Field(featuresJSON.items)
    #featuresList: list = Field(featuresList) 

class ProductUpdate(ProductBase):
    super.__init__()
    updatedAt: datetime = Field(default=get_time_to_utc)
    
class ProductDelete(ProductBase):
    """ Clase ProductDelete:  """
    deletedAt: datetime = Field(default_factory=get_time_to_utc)

