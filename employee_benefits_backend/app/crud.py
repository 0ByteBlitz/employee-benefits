# app/crud.py
from sqlalchemy.orm import Session

from . import models, schemas


# Employee CRUD operations
def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Benefit CRUD operations
def get_benefit(db: Session, benefit_id: int):
    return db.query(models.Benefit).filter(models.Benefit.id == benefit_id).first()

def get_benefits(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Benefit).offset(skip).limit(limit).all()

def create_benefit(db: Session, benefit: schemas.BenefitCreate):
    db_benefit = models.Benefit(**benefit.model_dump())
    db.add(db_benefit)
    db.commit()
    db.refresh(db_benefit)
    return db_benefit

# EmployeeBenefits CRUD operations
def get_employee_benefit(db: Session, employee_benefit_id: int):
    return db.query(models.EmployeeBenefits).filter(models.EmployeeBenefits.id == employee_benefit_id).first()

def get_employee_benefits(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.EmployeeBenefits).offset(skip).limit(limit).all()

def create_employee_benefit(db: Session, employee_benefit: schemas.EmployeeBenefitsCreate):
    db_employee_benefit = models.EmployeeBenefits(
        **employee_benefit.model_dump())
    db.add(db_employee_benefit)
    db.commit()
    db.refresh(db_employee_benefit)
    return db_employee_benefit

# StockGrant CRUD operations
def get_stock_grant(db: Session, stock_grant_id: int):
    return db.query(models.StockGrant).filter(models.StockGrant.id == stock_grant_id).first()

def get_stock_grants(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.StockGrant).offset(skip).limit(limit).all()

def create_stock_grant(db: Session, stock_grant: schemas.StockGrantCreate):
    db_stock_grant = models.StockGrant(**stock_grant.model_dump())
    db.add(db_stock_grant)
    db.commit()
    db.refresh(db_stock_grant)
    return db_stock_grant

# VestingRecord CRUD operations
def get_vesting_record(db: Session, vesting_record_id: int):
    return db.query(models.VestingRecord).filter(models.VestingRecord.id == vesting_record_id).first()

def get_vesting_records(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.VestingRecord).offset(skip).limit(limit).all()

def create_vesting_record(db: Session, vesting_record: schemas.VestingRecordCreate):
    db_vesting_record = models.VestingRecord(**vesting_record.model_dump())
    db.add(db_vesting_record)
    db.commit()
    db.refresh(db_vesting_record)
    return db_vesting_record
