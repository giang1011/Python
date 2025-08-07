from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    id: int
    name: str
    age: int
    grade: str

class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str