from sqlmodel import SQLModel, Field
from datetime import datetime
from utils.timestamps.DateTimeToUTC import get_time_to_utc
import uuid


class PlanBase(SQLModel):
    """ BASE PLAN CLASS """
    super.__init__() 
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    name: str | None = Field(max_length=100)
    description: str | None = Field(max_length=400)
    priceUF: float  | None = Field(nullable=False)
    isActive: bool | None = Field(nullable=False)
        
class PlanCreate(PlanBase):
    """ PlanCreate Model Based on PlanBase"""
    super.__init__()
    createdAt: datetime | None = Field(default_factory=get_time_to_utc, nullable=True)

class PlanStatus(PlanCreate):
    """
    Based on the model PlanCreate
    """
    super.__init__() 
    isActive: bool | None = Field(nullable=False)
    
class PlanUpdate(PlanBase and PlanStatus):
    """" """
    super.__init__()
    updatedAt: datetime = Field(default_factory=get_time_to_utc)
    
class PlanFeatures(PlanBase and PlanCreate): 
    """" """
    super.__init__()
    """ Costo mensual por DTE """
    monthly_dte: int | None = Field(max_length=50, nullable=False)
    """ Costo Adicional DTE en UF """
    cost_additional_dte_uf = Field(nullable=True)
    """ Numero Maximo de Sucursales"""
    max_branchs: int | None = Field(nullable=False)
    """ Cantidad maxima de Productos incluidos en el Plan""" 
    max_products: int | None = Field(nullable=False)
    """ Cantidad Maxima de Usuarios por plan"""
    max_warehouses: int | None = Field(nullable=False)
    """ Cantidad Maxima de Usuarios"""
    max_users: int | None = Field(nullable=False)    
    pass

class PlanRead(PlanBase and PlanCreate and PlanUpdate):
    """" """
    super.__init__()
    pass

class Plan(PlanRead): 
    """"""
    super.__init__()
    pass 