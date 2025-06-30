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