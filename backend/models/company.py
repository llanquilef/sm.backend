""" """
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from models.base import Base
from utils.timestamps.DateTimeToUTC import get_time_to_utc

# Base Company Class Model - Clase Base Empresa (Company)
class CompanyBase(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(100), max_length=100)
    schema = Column(max_length=100)
    createdAt = Column(DateTime(timezone=True), default=get_time_to_utc)
    updatedAt = Column(DateTime(timezone=True), default=get_time_to_utc)
    deletedAt = Column(DateTime(timezone=True), default=get_time_to_utc)