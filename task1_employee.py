import csv


# 1. Calculate bonus using normal, default, *args and **kwargs
def calculate_bonus(salary, rate=0.1, *extras, **options):
    bonus = salary * rate + sum(extras)

    if "cap" in options:
        bonus = min(bonus, options["cap"])

    return bonus


# 2. Employee class
class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def get_details(self):
        return f"{self.name} - {self.salary}"

    @property
    def annual_salary(self):
        return self.salary * 12


# 3. Decorator to log function calls
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


# 4. Manager inherits from Employee
class Manager(Employee):
    def __init__(self, name, department, salary, team_size):
        super().__init__(name, department, salary)
        self.team_size = team_size

    @log_call
    def get_details(self):
        return f"{self.name} - {self.salary} " f"- Team Size: {self.team_size}"


# 5. Read employee data from CSV
with open("employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    employees = list(reader)


# 6. Salary classification using conditions
for employee in employees:
    salary = int(employee["salary"])

    if salary < 50000:
        category = "Low Salary"
    elif salary < 70000:
        category = "Medium Salary"
    else:
        category = "High Salary"

    print(f"{employee['name']} - {category}")


# 7. Demonstrate bonus calculation
print("\nBonus Calculation:")
print(calculate_bonus(50000))
print(calculate_bonus(50000, 0.15, 1000, 2000, cap=8000))


# 8. Demonstrate Employee class and annual salary
employee1 = Employee("Arun", "Sales", 30000)

print("\nEmployee Details:")
print(employee1.get_details())
print("Annual Salary:", employee1.annual_salary)


# 9. Demonstrate Manager class and decorator
manager = Manager("Divya", "IT", 75000, 5)

print("\nManager Details:")
print(manager.get_details())
