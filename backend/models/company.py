from sqlmodel import SQLModel, Field
from datetime import datetime
from utils.timestamps.DateTimeToUTC import getTimeToUTC
import uuid

# Base Company Class Model - Clase Base Empresa (Company)
class CompanyBase(SQLModel): 
    id:  uuid.UUID = Field(default_factory= uuid.uuid4, primary_key=True)
    name: str = Field(max_length=100)
    schema: str = Field(max_length=100)

# Write Company Class - Clase Crear Empresa (Company)
class CompanyCreate(CompanyBase):
    createdAt: datetime | None = Field(default_factory=getTimeToUTC)

# Update Company Class
class CompanyUpdate(CompanyBase):
    updatedAt: datetime | None = Field(default_factory=getTimeToUTC)

class CompanyDelete(CompanyBase): 
    deletedAt: datetime | None = Field(default_factory=getTimeToUTC)
    isDeleted: bool = Field(default=True)
    
# Read Company Class 
class CompanyRead(CompanyBase and CompanyCreate and CompanyUpdate and CompanyDelete):
    pass

