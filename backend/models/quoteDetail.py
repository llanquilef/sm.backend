from sqlmodel import SQLModel, Field
import uuid 
from models.quote import QuoteBase
import datetime
from utils.timestamps.DateTimeToUTC import get_time_to_utc
#from inits.init_id import __initID__
from decimal import Decimal
 
def __init__(self, quote_detail: dict):
    self.quote_detail =  quote_detail
    return self.quote_detail

class QuoteDetailBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str = Field(max_length=80)
    description: str = Field(max_length=1000)
    quantity: Decimal = Field(nullable=False, max_digits=15, decimal_places=2)
    unit: str = Field(nullable=True)
    unitPrice: int = Field(nullable=True)
    
class QuoteDetailFK(QuoteDetailBase):
    """ 
    Clase QuoteDetailFK: Esta clase trae todos los atributos de su padre a traves de la herencia BaseMode
    Class QuoteDetailFK: Tihs class brings all the atributtes from his father across herency.
    """
    super.__init__()
    quoteId: uuid.UUID = Field(foreign_key=QuoteBase.id)
    
class QuoteDetailDiscount(QuoteDetailFK):
    super.__init__()
    discount: Decimal = Field(max_digits=10, decimal_places=2, nullable=True)
    type_discount: int = Field(nullable=True, default=0)
    exent: bool = Field(nullable=True, default=True)
    
class QuoteDetailCreate(QuoteDetailBase and QuoteDetailFK and QuoteDetailDiscount):
    """ 
    Clase QuoteDetailCreate: Esta clase trae todos los atributos necesarios para poder crear una cotizacion
    Class QuoteDetailCreate: Esta clase trae todos los atributos necesarios para poder crear una cotizacion 
    """
    super.__init__()
    createdAt:  datetime = Field(default_factory=get_time_to_utc)
    
class QuoteUpdate(QuoteDetailBase):
    super.__init__()
    updatedAt: datetime = Field(default_factory=get_time_to_utc)
    
class QuoteRead(QuoteDetailBase and QuoteUpdate): 
    super.__init__()
    pass

class QuoteDetail(QuoteRead and QuoteUpdate): 
    super.__init__()
    pass 

