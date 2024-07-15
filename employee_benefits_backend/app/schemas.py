from datetime import date
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    hire_date: date
    department: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BenefitBase(BaseModel):
    benefit_name: str
    description: str
    external_links: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class BenefitCreate(BenefitBase):
    pass


class Benefit(BenefitBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class EmployeeBenefitsBase(BaseModel):
    employee_id: int
    benefit_id: int
    start_date: date
    end_date: date

    model_config = ConfigDict(from_attributes=True)


class EmployeeBenefitsCreate(EmployeeBenefitsBase):
    pass


class EmployeeBenefits(EmployeeBenefitsBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class StockGrantBase(BaseModel):
    employee_id: int
    grant_date: date
    cliff_date: date
    shares_allocated: int
    vesting_schedule: str
    exercise_price: float

    model_config = ConfigDict(from_attributes=True)


class StockGrantCreate(StockGrantBase):
    pass


class StockGrant(StockGrantBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class VestingRecordBase(BaseModel):
    stock_grant_id: int
    vesting_date: date
    shares_vested: int
    shares_remaining: int

    model_config = ConfigDict(from_attributes=True)


class VestingRecordCreate(VestingRecordBase):
    pass


class VestingRecord(VestingRecordBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
