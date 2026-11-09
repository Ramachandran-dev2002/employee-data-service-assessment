import csv
import json
import logging
from pathlib import Path
from typing import List, Optional, Union

import fitz
from openpyxl import Workbook, load_workbook

# Configure logging
logging.basicConfig(level=logging.ERROR, format="%(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

# Get project folder location
BASE_DIR = Path(__file__).resolve().parent


# Read employee data from CSV
def load_employees() -> List[dict]:
    csv_file = BASE_DIR / "employees.csv"

    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        employees = list(reader)

    return employees


employees = load_employees()
print("Rows read:", len(employees))


# Write employee data to JSON
json_file = BASE_DIR / "employees.json"

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)


# Write high earners to CSV
high_earners = [employee for employee in employees if int(employee["salary"]) > 50000]

high_earners_file = BASE_DIR / "high_earners.csv"

with open(high_earners_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "department", "salary"])
    writer.writeheader()
    writer.writerows(high_earners)

print("High earners written:", len(high_earners))


# Create Excel file using openpyxl
excel_file = BASE_DIR / "salary.xlsx"

workbook = Workbook()
sheet = workbook.active
sheet.title = "Employee Salaries"

sheet.append(["Name", "Department", "Salary"])

for employee in employees:
    sheet.append([employee["name"], employee["department"], int(employee["salary"])])

workbook.save(excel_file)


# Read Excel file back
read_workbook = load_workbook(excel_file)
read_sheet = read_workbook.active

row_count = read_sheet.max_row - 1

print("salary.xlsx created and read back:", row_count, "rows")


# Extract text from first page of PDF
pdf_file = BASE_DIR / "assessment.pdf"

with fitz.open(pdf_file) as document:
    first_page = document[0]
    pdf_text = first_page.get_text()

print("PDF text:", pdf_text[:100])


# Read JSON file with exception handling
def read_file(path: Union[str, Path]) -> Optional[dict]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, dict):
                return data

            return None

    except FileNotFoundError:
        logger.error("File not found: %s", Path(path).name)

    except json.JSONDecodeError:
        logger.error("Invalid JSON file: %s", Path(path).name)

    return None


# Find employee by name
def find_employee(name: str) -> Optional[dict]:
    json_path = BASE_DIR / "employees.json"

    try:
        with open(json_path, "r", encoding="utf-8") as file:
            employee_list = json.load(file)

        for employee in employee_list:
            if employee["name"].lower() == name.lower():
                return employee

    except FileNotFoundError:
        logger.error("File not found: %s", json_path.name)

    except json.JSONDecodeError:
        logger.error("Invalid JSON file: %s", json_path.name)

    return None


# Test missing file handling
read_file(BASE_DIR / "missing.txt")
