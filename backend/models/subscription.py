from sqlmodel import Field, SQLModel
from datetime import datetime
from models.company import CompanyBase
from models.plan import PlanBase
from utils.timestamps.DateTimeToUTC import get_time_to_utc
import uuid

def __init__(self, subscription: dict):
    self.subscription = subscription
    return subscription  

STATUS = ['inactive', 'active', 'testing']
 
class SubscriptionBase(SQLModel):
    """ 
    Clase SubscriptionBase: Esta clase nos permite el obtener los atributos principales de la clase
    Class SubscriptionBase: This class allows to get all the principal attributes de la clase 
    """
    id: uuid.UUID = Field(default_factory= uuid.uuid4, primary_key=True)
    
class SubscriptionFK(SubscriptionBase): 
    super.__init__() 
    companyId: uuid.UUID = Field(foreign_key=CompanyBase.id)
    planId: uuid.UUID = Field(foreign_key=PlanBase.id)
         
class SubscritionCreate(SubscriptionBase):
    super.__init__()    
    ds: datetime | None = Field(default_factory=get_time_to_utc, nullable=False)
    de: datetime | None = Field(default_factory=get_time_to_utc, nullable=False)

class SubscriptionDelete(SubscriptionBase):
    super.__init__()
    deletedAt: datetime = Field(default_factory=get_time_to_utc)
    

class SubscriptionRead(SubscriptionBase):
    super.__init__()
    status: str = Field(STATUS, default=STATUS[1]) 
    
class Subscription(SubscriptionRead):
    super.__int__()


     
