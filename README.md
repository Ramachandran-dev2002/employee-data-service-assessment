# Employee Data Service

A Python-based Employee Data Service developed as part of the Week 1 Python + Software Engineering assessment.

## Project Overview

This project demonstrates Python fundamentals, file handling, API integration, security, object-oriented programming, and REST API development using FastAPI.

## Features

- Employee bonus calculation using functions, `*args`, and `**kwargs`.
- Employee and Manager classes using inheritance and decorators.
- CSV, JSON, Excel, and PDF file handling.
- API requests with retry handling using `requests`.
- HMAC-SHA256 webhook signature verification.
- REST API built with FastAPI.
- Automated tests using pytest.
- Code formatting and linting with Black and Ruff.
- Pre-commit hooks.

## Project Structure

```text
employee-service-assessment/
├── config/
├── docs/
├── scripts/
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── .env.example
├── .gitignore
├── .pre-commit-config.yaml
├── employees.csv
├── employees.json
├── high_earners.csv
├── pyproject.toml
├── requirements.txt
├── salary.xlsx
├── task1_employee.py
├── task2_file_handling.py
└── task3_api_security.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Ramachandran-dev2002/employee-data-service-assessment.git
cd employee-data-service-assessment
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Install development tools:

```bash
python -m pip install pytest-cov httpx2 black ruff pre-commit
```

## Environment Variables

Copy `.env.example` to `.env` and add your own values.

Never commit `.env` or real API credentials.

## Run the Tasks

```bash
python task1_employee.py
python task2_file_handling.py
python task3_api_security.py
```

## Run the FastAPI Application

```bash
python -m uvicorn src.main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## Run Tests

```bash
python -m pytest
```

Run tests with coverage:

```bash
python -m pytest --cov=src --cov-report=term-missing
```

## Code Quality

Run pre-commit checks:

```bash
python -m pre_commit run --all-files
```

## Technologies Used

- Python
- FastAPI
- Requests
- Pandas-independent CSV and JSON handling
- OpenPyXL
- PyMuPDF
- Pytest
- Black
- Ruff
- Git and GitHub

## Author

Developed as part of the Python + Software Engineering Week 1 assessment.