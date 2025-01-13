class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        return self.employees

    def remove_employees_by_age_range(self, min_age, max_age):
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]

    def find_employee_by_name(self, name):
        return next((emp for emp in self.employees if emp.name == name), None)

    def update_salary(self, name, new_salary):
        employee = self.find_employee_by_name(name)
        if employee:
            employee.salary = new_salary
            return True
        return False


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def run(self):
        while True:
            print("\n1. Add Employee")
            print("2. List Employees")
            print("3. Remove Employees by Age Range")
            print("4. Update Employee Salary")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                salary = float(input("Enter salary: "))
                self.manager.add_employee(Employee(name, age, salary))
                print("Employee added.")

            elif choice == "2":
                employees = self.manager.list_employees()
                if employees:
                    for emp in employees:
                        print(emp)
                else:
                    print("No employees found.")

            elif choice == "3":
                min_age = int(input("Enter minimum age: "))
                max_age = int(input("Enter maximum age: "))
                self.manager.remove_employees_by_age_range(min_age, max_age)
                print(f"Employees aged between {min_age} and {max_age} have been removed.")

            elif choice == "4":
                name = input("Enter employee name: ")
                new_salary = float(input("Enter new salary: "))
                if self.manager.update_salary(name, new_salary):
                    print("Salary updated.")
                else:
                    print("Employee not found.")

            elif choice == "5":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Try again.")



if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()