""" ADDITIONAL SERVICE MODEL"""
from sqlalchemy import Column, Numeric, Enum, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from models.conn_db import Base
from utils.timestamps.date_time_to_utc import get_time_to_utc


class AdditionalServiceBase(Base):
    """ Clase Create Additional Service Base """
    __tablename__ = 'additional_services'
    id = Column(UUID, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    priceUF = Column(Numeric(precision=10, scale=2))
    type = Column(Enum, nullable=False)
    createdAt = Column(DateTime(timezone=True), default=get_time_to_utc)
    updated_at = Column(DateTime(timezone=True), onupdate=get_time_to_utc)
