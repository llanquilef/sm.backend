import uuid
from sqlmodel import SQLModel, Field
from datetime import datetime 
from utils.timestamps.DateTimeToUTC import get_time_to_utc
from models.company import CompanyBase

def __init__(self, quoteDetail):  
    self.quoteDetail = quoteDetail
    return self.quoteDetail

class QuoteBase(SQLModel):
    super.__init__()
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    number: str = Field(unique=True)
    date: datetime = Field(default_factory=get_time_to_utc, nullable=False) 
    validUntil: datetime = Field(nullable=False)
    
class QuoteCreate(QuoteBase):
    super.__init__()
    subtotal: int = Field(default=0, nullable=False)
    tax: int = Field(default=0, nullable=False)
    total: int = Field(default=0, nullable=False)   
    createdAt: datetime = Field(default_factory=get_time_to_utc)
    companyId: uuid.UUID = Field(foreign_key=CompanyBase.id, nullable=False)

class QuoteNotes(): 
    super.__init__()
    notes: str | None = Field(default=None, max_length=1000)    

class QuoteUpdate(QuoteBase):
    super.__init__()
    updatedAt: datetime = Field(default_factory=get_time_to_utc)

class QuoteRead(QuoteBase and QuoteCreate and QuoteUpdate): 
    super.__init__()
    pass
  
class Quote(QuoteRead): 
   super.__init__()
   pass

class QuoteDelete(Quote):
    pass  
    