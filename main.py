from managers.manager import Manager
from models.employee import Employee

manager = Manager()
manager.load_managers()


print("***Sign in***")
username = input("Enter the username: ").lower().strip()
password = input("Enter the password: ").lower().strip()



logged_in = False
logged_manager = None
for admin in manager._Manager__managers:
    if admin._ManagerAccount__username == username and admin._ManagerAccount__password == password:
        logged_in = True
        logged_manager = admin
        break
        


if logged_in:
    employeesManager = Manager()
    employeesManager.load_employees()
    while True:
            print()
            print(f"Welcome, {logged_manager._ManagerAccount__name}!")
            print(f"-" * 19)
            print("# Choose an option: ")
            print(f"-" * 19)
            print("1. List admins")
            print("2. Add admin")
            print("3. remove admin")
            print("4. Exit")
            print()
            option = input("Your choice: ").strip()

            match option:
                case "1":
                    employeesManager.list_employees()
                case "2":
                    print()
                    employeesManager.load_employees()
                    employeeName = input("Enter the name: ")
                    employeeEmail = input("Enter the email: ")
                    employeePhone = input("Enter the phone: ")
                    employeePosition = input("Enter the position: ")
                    employeeID = input("Enter the ID: ")
                    new_employee = Employee(employeeName, employeeEmail, employeePhone, employeePosition, employeeID)
                    print()
                    employeesManager.add_employee(new_employee)
                case "3":
                    print()
                    employeeID = input("Enter the id to remove: ").strip()
                    if employeeID.isdigit():
                        employeesManager.remove_employee(employeeID)
                    else:
                        print("The ID must be a number.")
                    print()
                case "4":
                    break

                case _:
                    print()
                    "Invalid inputs"






   