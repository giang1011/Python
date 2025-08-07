from sqlalchemy import Column, Integer, String, Date
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50))
    middlename = Column(String(50))
    lastname = Column(String(50))
    birthday = Column(Date)
    phone = Column(String(20))
    email = Column(String(100))
