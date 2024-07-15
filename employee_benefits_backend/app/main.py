# app/main.py
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Employee endpoints
@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@app.get("/employees/", response_model=List[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees

@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# Benefit endpoints
@app.post("/benefits/", response_model=schemas.Benefit)
def create_benefit(benefit: schemas.BenefitCreate, db: Session = Depends(get_db)):
    return crud.create_benefit(db=db, benefit=benefit)

@app.get("/benefits/", response_model=List[schemas.Benefit])
def read_benefits(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    benefits = crud.get_benefits(db, skip=skip, limit=limit)
    return benefits

@app.get("/benefits/{benefit_id}", response_model=schemas.Benefit)
def read_benefit(benefit_id: int, db: Session = Depends(get_db)):
    db_benefit = crud.get_benefit(db, benefit_id=benefit_id)
    if db_benefit is None:
        raise HTTPException(status_code=404, detail="Benefit not found")
    return db_benefit

# EmployeeBenefits endpoints
@app.post("/employee_benefits/", response_model=schemas.EmployeeBenefits)
def create_employee_benefit(employee_benefit: schemas.EmployeeBenefitsCreate, db: Session = Depends(get_db)):
    return crud.create_employee_benefit(db=db, employee_benefit=employee_benefit)

@app.get("/employee_benefits/", response_model=List[schemas.EmployeeBenefits])
def read_employee_benefits(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employee_benefits = crud.get_employee_benefits(db, skip=skip, limit=limit)
    return employee_benefits

@app.get("/employee_benefits/{employee_benefit_id}", response_model=schemas.EmployeeBenefits)
def read_employee_benefit(employee_benefit_id: int, db: Session = Depends(get_db)):
    db_employee_benefit = crud.get_employee_benefit(db, employee_benefit_id=employee_benefit_id)
    if db_employee_benefit is None:
        raise HTTPException(status_code=404, detail="Employee Benefit not found")
    return db_employee_benefit

# StockGrant endpoints
@app.post("/stock_grants/", response_model=schemas.StockGrant)
def create_stock_grant(stock_grant: schemas.StockGrantCreate, db: Session = Depends(get_db)):
    return crud.create_stock_grant(db=db, stock_grant=stock_grant)

@app.get("/stock_grants/", response_model=List[schemas.StockGrant])
def read_stock_grants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    stock_grants = crud.get_stock_grants(db, skip=skip, limit=limit)
    return stock_grants

@app.get("/stock_grants/{stock_grant_id}", response_model=schemas.StockGrant)
def read_stock_grant(stock_grant_id: int, db: Session = Depends(get_db)):
    db_stock_grant = crud.get_stock_grant(db, stock_grant_id=stock_grant_id)
    if db_stock_grant is None:
        raise HTTPException(status_code=404, detail="Stock Grant not found")
    return db_stock_grant

# VestingRecord endpoints
@app.post("/vesting_records/", response_model=schemas.VestingRecord)
def create_vesting_record(vesting_record: schemas.VestingRecordCreate, db: Session = Depends(get_db)):
    return crud.create_vesting_record(db=db, vesting_record=vesting_record)

@app.get("/vesting_records/", response_model=List[schemas.VestingRecord])
def read_vesting_records(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    vesting_records = crud.get_vesting_records(db, skip=skip, limit=limit)
    return vesting_records

@app.get("/vesting_records/{vesting_record_id}", response_model=schemas.VestingRecord)
def read_vesting_record(vesting_record_id: int, db: Session = Depends(get_db)):
    db_vesting_record = crud.get_vesting_record(db, vesting_record_id=vesting_record_id)
    if db_vesting_record is None:
        raise HTTPException(status_code=404, detail="Vesting Record not found")
    return db_vesting_record
