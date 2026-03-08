""" CLIENT MODEL """
import uuid
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from models.conn_db import Base
from utils.timestamps.date_time_to_utc import get_time_to_utc


class ClientBase(Base):
    """ CLIENTS MODEL """
    __tablename__ = 'clients'
    id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name = Column(String(100))
    # Buscar mejor convencion de nombre para este atributo
    rut = Column(String(12), nullable=False)
    socialReason = Column(String(100), nullable=False)
    businessLine = Column(String(100), nullable=False)
    city = Column(Integer, nullable=True)
    direction = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True)
    phone = Column(String(12), nullable=True)
    notes = Column(String(1000), nullable=True)
    companyId = Column(UUID(as_uuid=True), ForeignKey('companies.id'))
    createdAt = Column(DateTime(timezone=True), default=get_time_to_utc, 
                       nullable=False)
    updatedAt = Column(DateTime(timezone=True), onupdate=get_time_to_utc)
