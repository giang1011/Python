from pydantic import BaseModel
from datetime import date

class EmployeeBase(BaseModel):
    firstname: str
    middlename: str
    lastname: str
    birthday: date
    phone: str
    email: str

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
