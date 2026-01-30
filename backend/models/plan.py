from sqlmodel import SQLModel, Field
from datetime import datetime
from utils.DateTimeToUTC import getTimeToUTC

class BasePlan(SQLModel): 
    id: int = Field(primary_key=True)
    name: str = Field(max_length=100)
    description: str = Field(max_length=400)
    priceUF: float
    createdAt: datetime | None = Field(default_factory=getTimeToUTC)
    