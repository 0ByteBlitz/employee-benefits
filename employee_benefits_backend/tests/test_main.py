import logging

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_create_employee():
    response = client.post(
        "/employees/",
        json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "hire_date": "2022-01-01",
            "department": "Engineering"
        },
    )
    assert response.status_code == 200
    assert response.json()["email"] == "johndoe@example.com"

def test_read_employees():
    response = client.get("/employees/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_benefit():
    response = client.post(
        "/benefits/",
        json={
            "benefit_name": "Health Insurance",
            "description": "Full health coverage",
            "external_links": "http://example.com"
        },
    )
    assert response.status_code == 200
    assert response.json()["benefit_name"] == "Health Insurance"

def test_read_benefits():
    response = client.get("/benefits/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_employee_benefit():
    response = client.post(
        "/employee_benefits/",
        json={
            "employee_id": 1,
            "benefit_id": 1,
            "start_date": "2022-01-01",
            "end_date": "2023-01-01"
        },
    )
    assert response.status_code == 200
    assert response.json()["employee_id"] == 1

def test_read_employee_benefits():
    response = client.get("/employee_benefits/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_stock_grant():
    response = client.post(
        "/stock_grants/",
        json={
            "employee_id": 1,
            "grant_date": "2022-01-01",
            "cliff_date": "2023-01-01",
            "shares_allocated": 1000,
            "vesting_schedule": "quarterly",
            "exercise_price": 10.5
        },
    )
    assert response.status_code == 200
    assert response.json()["shares_allocated"] == 1000

def test_read_stock_grants():
    response = client.get("/stock_grants/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_vesting_record():
    response = client.post(
        "/vesting_records/",
        json={
            "stock_grant_id": 1,
            "vesting_date": "2022-01-01",
            "shares_vested": 250,
            "shares_remaining": 750
        },
    )
    assert response.status_code == 200
    assert response.json()["shares_vested"] == 250

def test_read_vesting_records():
    response = client.get("/vesting_records/")
    assert response.status_code == 200
    assert len(response.json()) > 0
