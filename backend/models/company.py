from sqlmodel import SQLModel, Field
from datetime import datetime
from utils.DateTimeToUTC import getTimeToUTC


class BaseCompany(SQLModel): 
    id: int = Field(primary_key=True)
    name: str = Field(max_length=100)
    schema: str = Field(max_length=100)

class CompanyCreate(BaseCompany):
    createdAt: datetime | None = Field(default_factory=getTimeToUTC)


