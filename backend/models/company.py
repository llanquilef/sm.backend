""" COMPANY MODEL """
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime, Boolean
from models.conn_db import Base
from utils.timestamps.date_time_to_utc import get_time_to_utc


class CompanyBase(Base):
    """ Clase CompanyBase
        CompanyBase Class
    """
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    name = Column(String(100), nullable=False)
    schema = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), default=get_time_to_utc, 
                        nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=get_time_to_utc, 
                        nullable=True)
    deleted_at = Column(DateTime(timezone=True), default=get_time_to_utc, 
                        nullable=True)
    is_active = Column(Boolean, default=True)
