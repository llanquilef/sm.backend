from  sqlmodel import SQLModel, Field 
import uuid
from models.client import Client
from models.company import CompanyBase

def __init__(self, id: uuid.uuid4) -> id:
    self.id = id
    return self.id


class ClientBase(SQLModel):
    super.__init__()
    id: uuid.UUID = Field(default_factory=Client(id))
    name: str = Field(max_length=100)
    rut: str = Field(max_length=12)

class ClientCreate(ClientBase): 
    super.__init__()
    companyId = uuid.UUID = Field(foreign_key=CompanyBase.id)
    socialReason: str = Field(max_length=100, nullable=False)
    businessLine: str = Field(max_length=100, nullable=False)
    city: int = Field(nullable=True)
    direction: str = Field(max_length=100, nullable=False)
    email: str = Field(max_length=100)
    phone: str = Field(max_length=12)

class ClientNotes(ClientBase and ClientCreate):
    super.__init__()
    notes = str = Field(nullable=True)
    
class ClientRead(ClientBase and ClientCreate and ClientNotes):
    super.__init__()
    pass

    

        
    