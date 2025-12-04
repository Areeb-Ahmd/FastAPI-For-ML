#We implement pydantic data models for our employee application.
from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    department: str
    age: int