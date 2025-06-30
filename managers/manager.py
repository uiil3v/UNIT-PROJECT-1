import json
from models.employee import Employee
from models.menu import Menu
from models.managerAccount import ManagerAccount

class Manager:

    def __init__ (self):
        self.__employees = []
        self.__managers = []
        self.menu = Menu

        
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
        print("New employee has been added, successfully.")
    
    def remove_employee(self, id: str):
        removed = None
        for employee in self.__employees:
            if employee._Employee__id == id:
                removed = employee
                break
        
        if removed:
            self.__employees = [employee for employee in self.__employees if employee._Employee__id != id]
            self.save_employees()
            print(f"{removed._Employee__name} whose ID: {id}, has been removed successfully.")
        else:
            print(f"No employee found with ID: {id}")
    
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
                            print(f"Name changed to {new_name} successfully.")
                        case "2":
                            new_email = input("Enter the new email(@gmail, @hotmail, or @outlook): ").lower().strip()
                            if new_email.endswith(("@gmail.com", "@hotmail.com" , "@outlook.com")):
                                emp._Employee__email = new_email
                                print(f"Email changed to {new_email} successfully.")
                            else:
                                print("Invalid email domain.")
                        case "3":
                            new_phone = input("Enter the new phone(05********): ")
                            if new_phone.startswith("05") and new_phone.isdigit() and len(new_phone) == 10:
                                emp._Employee__phone = new_phone
                                print(f"Phone changed to {new_phone} successfully.")
                            else:
                                print("Invalid phone number.")
                        case "4":
                            new_position = input("Enter the new position: ")
                            emp._Employee__position = new_position
                        case "5":
                            new_id = input("Enter the new ID: ").strip()
                            if new_id.isdigit():
                                emp._Employee__id = new_id
                            print(f"ID changed to {new_id} successfully.")
                        case "6":
                            break
                        case _:
                            print("Invalid input.")
                self.save_employees()
                break
        if not found:
            print("The ID not found!")
    
    def list_employees(self):
        if not self.__employees:
            print("No employees found.")
            return
        for index, data in enumerate(self.__employees , start=1):
            print()
            print(f"# Employee {index}:")
            print(f"- Name: {data._Employee__name}")
            print(f"- Email: {data._Employee__email}")
            print(f"- Phone: {data._Employee__phone}")
            print(f"- Position: {data._Employee__position}")
            print(f"- ID: {data._Employee__id}")
            print()

    def add_dish(self, dish: str, price: float):
        self.menu.add_dish(dish, price)

    def remove_dish (self, dish: str):
        self.menu.remove_dish(dish)

    def update_dish (self, dish: str, new_price: float):
        self.menu.update_dish(dish, new_price)

    def display_menu(self):
        self.menu.display_menu()