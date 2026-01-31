from sqlmodel import SQLModel, Field 
import uuid
from utils.timestamps.DateTimeToUTC import getTimeToUTC
from models.company import CompanyBase
from models.supplier import SupplierBase
import datetime 

def __init__(id: uuid.uuid4):
    return id

class ProductBase(SQLModel):
    id: uuid.UUID = Field(primary_key=True, nullable=False)
    name: str = Field(max_length=100, nullable=False)
    description: str = Field(max_length=400)
    
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

class ProductCreate(ProductBase):
    super.__init__()
    companyId: Field(foreign_key=CompanyBase.id)
    supplierId: Field(foreign_key=SupplierBase.id)
    createdAt: str = Field(default_factory=getTimeToUTC)
    #featuresDict: dict = Field(featuresJSON.items)
    #featuresList: list = Field(featuresList) 
    
class ProductUpdate(ProductBase): 
    super.__init__()
    updatedAt: datetime = Field(default=getTimeToUTC)
    
class ProductDelete(ProductBase):
    super.__init__()
    pass

