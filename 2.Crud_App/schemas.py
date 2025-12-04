from pydantic import BaseModel, EmailStr, ConfigDict

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True) 