import datetime
import uuid 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Numeric, Integer
from base import Base
from utils.timestamps.DateTimeToUTC import get_time_to_utc


"""" Debo agregar los types apenas defina cuales seran """
TYPES = []

class AdditionalServiceBase(Base):
    """ Clase Create Additional Service Base """ 
    id =  Column(UUID(as_uuid=True), 
                 primary_key=True, 
                 nullable=False, 
                 default=uuid.uuid4
                 )
    name = Column(String(100), 
                  nullable=False)
    priceUF = (Numeric(precision=10, scale=2))
    """ Voy a manejar los types con integer y crear un mapper """
    type = Column(Integer, nullable=False)
    createdAt = Column(default=get_time_to_utc, nullable=False)

class AdditionalServiceUpdate(AdditionalServiceBase): 
    updatedAt = Column(default=get_time_to_utc, nullable=False)


    