#We implement pydantic data models for our employee application.
from pydantic import BaseModel, Field, StrictInt
from typing import Optional

class Employee(BaseModel):
    id: int = Field(..., gt=0, description="The ID must be a positive integer")
    name: str = Field(..., min_length=3, max_length=50)
    department: str = Field(..., min_length=2, max_length=30)
    age: Optional[StrictInt] = Field(default = None, ge = 21)
