import json
from pathlib import Path
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Employee Data Service")

BASE_DIR = Path(__file__).resolve().parent.parent
EMPLOYEES_FILE = BASE_DIR / "employees.json"


# Validate incoming employee data
class EmployeeCreate(BaseModel):
    name: str = Field(min_length=1)
    department: str
    salary: float = Field(gt=0)


# Read employees from JSON file
def load_employees() -> List[dict]:
    if not EMPLOYEES_FILE.exists():
        return []

    with open(EMPLOYEES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# Save employees to JSON file
def save_employees(employees: List[dict]) -> None:
    with open(EMPLOYEES_FILE, "w", encoding="utf-8") as file:
        json.dump(employees, file, indent=4)


# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}


# Get all employees
@app.get("/employees")
def get_employees():
    return load_employees()


# Get one employee by name
@app.get("/employees/{name}")
def get_employee(name: str):
    employees = load_employees()

    for employee in employees:
        if employee["name"].lower() == name.lower():
            return employee

    raise HTTPException(status_code=404, detail="Employee not found")


# Add a new employee
@app.post("/employees")
def create_employee(employee: EmployeeCreate):
    employees = load_employees()

    new_employee = employee.model_dump()
    employees.append(new_employee)

    save_employees(employees)

    return {"message": "Employee added successfully", "employee": new_employee}
