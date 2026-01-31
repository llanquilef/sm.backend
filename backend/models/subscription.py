from sqlmodel import Field, SQLModel
from datetime import datetime
from models.company import CompanyBase as BaseCompany
from models.plan import PlanBase
from utils.timestamps.DateTimeToUTC import get_time_to_utc
import uuid

def __init__(self, subscription: dict):
    self.subscription = subscription
    return subscription  

STATUS = ['inactive', 'active', 'testing']
 
class SubscriptionBase(SQLModel): 
    super.__init__()
    id: uuid.UUID = Field(default_factory= uuid.uuid4, primary_key=True)
    companyId: int = Field(foreign_key=BaseCompany.id)
    planId: int = Field(foreign_key=PlanBase.id)
    
class SubscritionCreate(SubscriptionBase):
    super.__init__()
    ds: datetime | None = Field(default_factory=get_time_to_utc, nullable=False)
    de: datetime | None = Field(default_factory=get_time_to_utc, nullable=False)

class SubscriptionRead(SubscriptionBase and SubscritionCreate):
    super.__init__()
    status: str = Field(STATUS, default=STATUS[1]) 
    pass

class Subscription(SubscriptionRead):
    super.__int__()
    pass 
     
