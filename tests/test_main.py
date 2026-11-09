from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


# Test 1: Health check
def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


# Test 2: Get all employees
def test_get_all_employees():
    response = client.get("/employees")

    assert response.status_code == 200
    assert len(response.json()) >= 5


# Test 3: Find an existing employee
def test_get_employee():
    response = client.get("/employees/Arun")

    assert response.status_code == 200
    assert response.json()["name"] == "Arun"


# Test 4: Employee not found
def test_employee_not_found():
    response = client.get("/employees/Ravi")

    assert response.status_code == 404
    assert response.json()["detail"] == "Employee not found"


# Test 5: Invalid salary
def test_invalid_salary():
    employee = {"name": "Test Employee", "department": "IT", "salary": -5}

    response = client.post("/employees", json=employee)

    assert response.status_code == 422


# Test 6: Empty employee name
def test_empty_name():
    employee = {"name": "", "department": "IT", "salary": 30000}

    response = client.post("/employees", json=employee)

    assert response.status_code == 422
