import datetime 
import uuid 
from sqlmodel import SQLModel, Field
from utils.timestamps.DateTimeToUTC import get_time_to_utc
from utils.utc_to_string import format_UTC_to_string

"""" Debo agregar los types apenas defina cuales seran """
TYPES = []

class AdditionalServiceBase(SQLModel):
    """""" 
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    priceUF: float = Field(nullable=False)
    type: enumerate = Field(TYPES, default=TYPES[0],  nullable=False)
    
    
class AdditionalServiceCreate(AdditionalServiceBase):
    """"""
    super.__init__()
    createdAt: datetime = Field(default_factory=get_time_to_utc)

class AdditionalServiceUpdate(AdditionalServiceCreate):
    super.__init__()
    updatedAt = datetime = Field(default_factory=get_time_to_utc)  


class AdditionalRead(AdditionalServiceBase and AdditionalServiceCreate):
    pass
     
class AdditionalService(AdditionalRead):
    super.__init__()
    




    