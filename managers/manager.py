import json
from models.employee import Employee
from models.managerAccount import ManagerAccount

class Manager:
    
    def __init__ (self):
        self.__employees = []
        self.__managers = []

        
    def load_managers(self):
        try:
            with open("data/managers.json", "r", encoding="UTF-8") as file:
                data = json.load(file)
                self.__managers = [ManagerAccount.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.__managers = []


    def load_employees(self):
        try:
            with open("data/employees.json" ,"r" , encoding="UTF-8") as file:
                data = json.load(file)
                self.__employees = [Employee.from_dict(item) for item in data]
        except FileNotFoundError:
            self.__employees = []

    def save_employees(self):
        with open("data/employees.json", "w" , encoding="UTF-8") as file:
            data = [employee.to_dict() for employee in self.__employees]
            json.dump(data , file , indent=4)
    
    def add_employee(self, employee: Employee):
        self.__employees.append(employee)
        self.save_employees()
        print("- New employee has been added successfully.")
    
    def remove_employee(self, id: str):
        removed = None
        for employee in self.__employees:
            if employee._Employee__id == id:
                removed = employee
                break
        
        if removed:
            self.__employees = [employee for employee in self.__employees if employee._Employee__id != id]
            self.save_employees()
            print()
            print(f"- Employee '{removed._Employee__name}' with ID: {id}, has been removed successfully.")
        else:
            print()
            print(f"- No employee found with ID: {id}.")
    
    def update_employee_info(self):
        employeeID = input("Enter the employee ID to update: ").strip()
        found = False
        for emp in self.__employees:
            if emp._Employee__id == employeeID:
                found = True
                while True:
                    print()
                    print("Which information do you want to update?")
                    print("1. Name")
                    print("2. Email")
                    print("3. Phone")
                    print("4. Position")
                    print("5. ID")
                    print("6. Exit")
                    print()

                    choice = input("Enter your choice: ")

                    match choice:
                        case "1":
                            new_name = input("Enter the new name: ")
                            emp._Employee__name = new_name
                            print()
                            print(f"- Name changed to {new_name} successfully.")
                        case "2":
                            new_email = input("Enter the new email(@gmail, @hotmail, or @outlook): ").lower().strip()
                            if new_email.endswith(("@gmail.com", "@hotmail.com" , "@outlook.com")):
                                emp._Employee__email = new_email
                                print()
                                print(f"- Email changed to {new_email} successfully.")
                            else:
                                print()
                                print("- Invalid email domain.")
                        case "3":
                            new_phone = input("Enter the new phone(05********): ")
                            if new_phone.startswith("05") and new_phone.isdigit() and len(new_phone) == 10:
                                emp._Employee__phone = new_phone
                                print()
                                print(f"- Phone changed to {new_phone} successfully.")
                            else:
                                print()
                                print("- Invalid phone number.")
                        case "4":
                            new_position = input("Enter the new position: ")
                            emp._Employee__position = new_position
                            print()
                            print(f"- Position changed to {new_position} successfully.")
                        case "5":
                            new_id = input("Enter the new ID(numbers): ").strip()
                            if new_id.isdigit():
                                emp._Employee__id = new_id
                                print()
                                print(f"- ID changed to {new_id} successfully.")
                            else:
                                print()
                                print("- Invalid inputs.")
                        case "6":
                            break
                        case _:
                            print("- Invalid input.")
                self.save_employees()
                break
        if not found:
            print()
            print("- The ID not found!")
    
    def list_employees(self):
        if not self.__employees:
            print("- No employees found.")
            return
        print()
        print("---- Employees ----")
        for index, data in enumerate(self.__employees , start=1):
            print()
            print(f"# Employee {index}:")
            print(f"- Name: {data._Employee__name}")
            print(f"- Email: {data._Employee__email}")
            print(f"- Phone: {data._Employee__phone}")
            print(f"- Position: {data._Employee__position}")
            print(f"- ID: {data._Employee__id}")
            print()