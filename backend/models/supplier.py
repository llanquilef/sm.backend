from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import uuid4
import uuid 
from utils.timestamps.DateTimeToUTC import get_time_to_utc
from models.company import CompanyBase

# Supplier Base Model
class SupplierBase(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    category: str = Field(max_length=50)
    businessLine: str = Field(max_length=100)
    
# Supplier Create Model
class SupplierCreate(SupplierBase):
    email: str = Field(max_length=100)
    taxId: str = Field(max_length=100)
    companyId: uuid.UUID = Field(foreign_key=CompanyBase.id)
    createdAt: datetime = Field(default_factory=get_time_to_utc)

# Supplier Update Model 
class SupplierUpdate(SupplierBase):
    uptadedAt: datetime = Field(default_factory=get_time_to_utc)

# Supplier Delete Model
class SupplierDelete(SupplierBase): 
    deletedAt: datetime = Field(default_factory=get_time_to_utc)
    isDeleted: bool = Field(default=True)
    
# Supplier Read Model 
class SupplierRead(SupplierBase and SupplierCreate and SupplierDelete):
    pass