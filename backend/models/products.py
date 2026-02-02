from sqlmodel import SQLModel, Field, Relationship
import uuid
from utils.timestamps.DateTimeToUTC import get_time_to_utc
from models.company import CompanyBase
from models.supplier import SupplierBase
import datetime 

UNITS_ENUMS = ['kg', 'un', 'gr', 'litro', 'ml', 'caja']

class ProductBase(SQLModel):
    """ 
    Clase ProductBase: Define clase base de Products
    ProductBase Class: Define base class of products
    """
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    name: str = Field(max_length=100, nullable=False)
    description: str = Field(max_length=400, nullable=True)
    sku: str = Field(default=0, nullable=False)
    stockQuantity: int = Field(default=0, nullable=False)
    unit: enumerate = Field(default=UNITS_ENUMS[0], nullable=False)
    buyPrice: float = Field(default=0.0, nullable=False)
    salePrice: float = Field(default=0.0, nullable=False)
    minStockLevel: int = Field(default=0, nullable=True)
    profitMargin: float = Field(default=0.0, nullable=True)
     
class ProductCategories():
    """ Se define clase ProductCategories que hereda desde su padre en arbol con la funcion add_child() """ 
    name: str = Field(nullable=False)

class ProductStatus():
    """ Se define clase ProductStatus que hereda desde su padre en arbol ProductBase"""" 
    status: bool = Field(default=True)
    
class ProductFoodCategory():
    """ Se define clase ProductFood Categories que lo recibe desde su nodo padre(2) -> ProductCategories """
    hasFifoRules: bool = Field(default=False)
    
class ProductToolCategory():
    """ Se define clase ProductToolCategory como hijo de ProductCategories """ 
    
class ProductFK(ProductBase): 
    super.__init__()
    companyId: uuid.UUID = Relationship(CompanyBase.id) 
    supplierId: uuid.UUID = Relationship(SupplierBase.id)

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
    super.__init__()
    deletedAt: datetime = Field(default_factory=get_time_to_utc)

