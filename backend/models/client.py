""" CLIENT CLASS """
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from models.base import Base
from models.company import CompanyBase
from utils.timestamps.DateTimeToUTC import get_time_to_utc

class ClientBase(Base):
    __tablename__ = 'clients'
    """ CLIENT MODEL BASE """
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    taxId = Column(String(12), nullable=False) 
    companyId = ForeignKey(CompanyBase.id, ondelete='CASCADE')
    socialReason = Column(String(100), nullable=False)
    businessLine = Column(String(100), nullable=True)
    district = Column(Integer, nullable=True) 
    city = Column(Integer, nullable=True)
    address = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    phone = Column(String(12), nullable=True)
    notes = Column(Text, 
                   nullable=True, 
                   comment='Notas o comentarios adicionales sobre el cliente')

class ClientCreate(ClientBase): 
    """ CLIENT CREATE CLASS -> Deriva de ClientBase """
    created_at = Column(DateTime(timezone=True), 
                        nullable=False, 
                        default=get_time_to_utc) 

class ClientUpdate(ClientBase): 
    """ CLIENT CREATE CLASS -> Deriva de ClientBase """
    updated_at = Column(DateTime(timezone=True), 
                        nullable=False, 
                        default=get_time_to_utc)    