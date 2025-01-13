import json

class EmployeesManagerWithFile(EmployeesManager):
    def __init__(self, filename="employees.json"):
        super().__init__()
        self.filename = filename
        self.load_employees()

    def save_employees(self):
        with open(self.filename, "w") as file:
            data = [{"name": emp.name, "age": emp.age, "salary": emp.salary} for emp in self.employees]
            json.dump(data, file)

    def load_employees(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.employees = [Employee(emp["name"], emp["age"], emp["salary"]) for emp in data]
        except FileNotFoundError:
            self.employees = []

    def add_employee(self, employee):
        super().add_employee(employee)
        self.save_employees()

    def remove_employees_by_age_range(self, min_age, max_age):
        super().remove_employees_by_age_range(min_age, max_age)
        self.save_employees()

    def update_salary(self, name, new_salary):
        if super().update_salary(name, new_salary):
            self.save_employees()
            return True
        return False


class FrontendManagerWithAuth:
    def __init__(self):
        self.manager = EmployeesManagerWithFile()
        self.logged_in = False

    def login(self):
        print("Please log in.")
        username = input("Username: ")
        password = input("Password: ")
        if username == "admin" and password == "admin":
            print("Login successful.")
            self.logged_in = True
        else:
            print("Invalid credentials.")

    def run(self):
        self.login()
        if not self.logged_in:
            return

        while True:
            print("\n1. Add Employee")
            print("2. List Employees")
            print("3. Remove Employees by Age Range")
            print("4. Update Employee Salary")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter name: ")
                try:
                    age = int(input("Enter age: "))
                    salary = float(input("Enter salary: "))
                    self.manager.add_employee(Employee(name, age, salary))
                    print("Employee added.")
                except ValueError:
                    print("Invalid input. Age and salary must be numeric.")

            elif choice == "2":
                employees = self.manager.list_employees()
                if employees:
                    for emp in employees:
                        print(emp)
                else:
                    print("No employees found.")

            elif choice == "3":
                try:
                    min_age = int(input("Enter minimum age: "))
                    max_age = int(input("Enter maximum age: "))
                    self.manager.remove_employees_by_age_range(min_age, max_age)
                    print(f"Employees aged between {min_age} and {max_age} have been removed.")
                except ValueError:
                    print("Invalid input. Age must be numeric.")

            elif choice == "4":
                name = input("Enter employee name: ")
                try:
                    new_salary = float(input("Enter new salary: "))
                    if self.manager.update_salary(name, new_salary):
                        print("Salary updated.")
                    else:
                        print("Employee not found.")
                except ValueError:
                    print("Invalid input. Salary must be numeric.")

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Try again.")



if __name__ == "__main__":
    frontend = FrontendManagerWithAuth()
    frontend.run()
