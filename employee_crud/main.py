from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/", response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@app.get("/employees/", response_model=list[schemas.EmployeeOut])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{employee_id}", response_model=schemas.EmployeeOut)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_emp = crud.get_employee(db, employee_id)
    if not db_emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_emp

@app.put("/employees/{employee_id}", response_model=schemas.EmployeeOut)
def update_employee(employee_id: int, emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_emp = crud.update_employee(db, employee_id, emp)
    if not db_emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_emp

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_emp = crud.delete_employee(db, employee_id)
    if not db_emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}
