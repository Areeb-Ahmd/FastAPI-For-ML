import models, schemas, crud
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal, Base
from typing import List

#Create the database tables
Base.metadata.create_all(bind=engine)

#Initialize FastAPI app
app = FastAPI()

#Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#API endpoint to create a new employee
@app.post("/employees/", response_model = schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

#API endpoint to get all employees
@app.get("/employees/", response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

#API endpoint to get a single employee by ID
@app.get("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found.")
    return employee

#API endpoint to update an existing employee
@app.put("/employees/{emp_id}", response_model=schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.update_employee(db, emp_id, employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found.")
    return db_employee

#API endpoint to delete an employee
@app.delete("/employees/{emp_id}", response_model = dict)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = crud.delete_employee(db, emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee Not Found.")
    return {"detail": "Employee Deleted Successfully."}
