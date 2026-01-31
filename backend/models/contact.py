from sqlmodel import SQLModel, Field
import uuid
from utils.timestamps.DateTimeToUTC import get_time_to_utc
from models.company import CompanyBase
from datetime import datetime 

TYPES_CONTACTS = ['provider', 'tranpsort', 'employee', 'others'] 

class ContactBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str = Field(nullable=False)
    taxId: str = Field(nullable=False)
    type: enumerate = Field(default=TYPES_CONTACTS, nullable=False)
    email: str = Field(nullable=False)
    
class ContactCreate(ContactBase):
    #userId: uuid.UUID = Field(foreign_key=True)
    companyId: uuid.UUID = Field(foreign_key=CompanyBase.id)
    createdAt: datetime = Field(default_factory=get_time_to_utc)
    
class ContactUpdate(ContactBase):
    updatedAt: datetime = Field(default_factory=get_time_to_utc)    

class ContactNotes(ContactBase):
    notes: str = Field(max_length=1000)
    