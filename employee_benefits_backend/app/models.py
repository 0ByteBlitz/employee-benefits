# app/models.py
from sqlalchemy import DECIMAL, Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hire_date = Column(Date, nullable=False)
    department = Column(String)


class Benefit(Base):
    __tablename__ = 'benefit'
    id = Column(Integer, primary_key=True, index=True)
    benefit_name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    external_links = Column(String)


class EmployeeBenefits(Base):
    __tablename__ = 'employee_benefits'
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    benefit_id = Column(Integer, ForeignKey('benefit.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)


class StockGrant(Base):
    __tablename__ = 'stock_grant'
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    grant_date = Column(Date, nullable=False)
    cliff_date = Column(Date, nullable=False)
    shares_allocated = Column(Integer, nullable=False)
    vesting_schedule = Column(String, nullable=False)
    exercise_price = Column(DECIMAL, nullable=False)


class VestingRecord(Base):
    __tablename__ = 'vesting_record'
    id = Column(Integer, primary_key=True, index=True)
    stock_grant_id = Column(Integer, ForeignKey(
        'stock_grant.id'), nullable=False)
    vesting_date = Column(Date, nullable=False)
    shares_vested = Column(Integer, nullable=False)
    shares_remaining = Column(Integer, nullable=False)
