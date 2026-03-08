""" QUOTE MODEL """
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from utils.timestamps.date_time_to_utc import get_time_to_utc
from models.company import CompanyBase
from models.conn_db import Base


class QuoteBase(Base):
    """ QuoteBase Class"""
    __tablename__ = 'quotes'
    id = Column(UUID(as_uuid=True), primary_key=True)
    number = Column(Integer)
    date = Column(DateTime(timezone=True), default=get_time_to_utc)
    validUntil = Column(DateTime(timezone=True), nullable=False)
    subtotal = Column(Integer, default=0, nullable=False)
    tax = Column(Integer, default=0, nullable=False)
    total = Column(Integer, default=0, nullable=False)
    notes = Column(String(1000))
    companyId = ForeignKey(UUID(as_uuid=True), CompanyBase.id)
    created_at = Column(DateTime(timezone=True), default=get_time_to_utc)
    updated_at = Column(DateTime(timezone=True), default=get_time_to_utc)
    deletedAt = Column(DateTime(timezone=True), default=get_time_to_utc)
