import datetime 
import uuid 
from sqlmodel import SQLModel, Field
from utils.timestamps.DateTimeToUTC import get_time_to_utc
from utils.utc_to_string import format_UTC_to_string

"""" Debo agregar los types apenas defina cuales seran """
TYPES = []

class AdditionalServiceBase(SQLModel):
    """ Clase Create Additional Service Base """ 
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    priceUF: float = Field(nullable=False)
    type: enumerate = Field(TYPES, default=TYPES[0],  nullable=False)
    
class AdditionalServiceCreate(AdditionalServiceBase):
    """ Class Create AdditionalService - Clase Create AdditionalService """
    super.__init__()
    createdAt: datetime = Field(default_factory=get_time_to_utc)

class AdditionalServiceUpdate(AdditionalServiceCreate):
    """ Class Create AdditionalServiceUpdate - Clase Create AdditionalServiceUpdate """
    super.__init__()
    updatedAt = datetime = Field(default_factory=get_time_to_utc)  


class AdditionalServiceRead(AdditionalServiceBase and AdditionalServiceCreate and AdditionalServiceUpdate):
    """
    Class Create AdditionalRead - Clase CreateAdditionalServiceRead
    
    PUNTO A CONSIDERAR: Aqui debo crear una funcion que al llamarla me permita solo la lectura
                        Debe ir como parametro de clase y no como funcion ya que tendria que por cada funcion 
                        generar esa variable o crear una funcon auxiliar 
    """
    super.__init__()
    pass
     

class AdditionalService(AdditionalServiceRead):
    """
    Class AdditionalService() - Clase AdditionalService
    """
    super.__init__()
    pass 


    




    