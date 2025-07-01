from managers.manager import Manager
from models.employee import Employee
from models.menu import Menu

manager = Manager()
manager.load_managers()

logged_in = False
logged_manager = None
while True:
    print()
    print("***** SIGN IN *****")
    username = input("Enter the username: ").lower().strip()
    password = input("Enter the password: ").lower().strip()

    for admin in manager._Manager__managers:
        if admin._ManagerAccount__username == username and admin._ManagerAccount__password == password:
            logged_in = True
            logged_manager = admin
            break

    if logged_in:
        break
    else:
        print()
        print("- Wrong username or password. Please try again.")
       

employeesManager = Manager()
employeesManager.load_employees()
menuManager = Menu()
menuManager.load_menu()

if logged_in:

    while True:
        print()
        print(f"- Welcome {logged_manager._ManagerAccount__name}!")
        print()
        print(f"-" * 19)
        print("# Choose an option: ")
        print(f"-" * 19)
        print("1. Employee Settings")
        print("2. Menu Settings")
        print("3. Exit")
        print()
        
        option = input("Your choice: ").strip()

        match option:
            case "1":

                while True:
                    print()
                    print(f"-" * 19)
                    print("# Choose an option: ")
                    print(f"-" * 19)
                    print("1. List Employees")
                    print("2. Add Employee")
                    print("3. Remove Employee")
                    print("4. Update Employee Information")
                    print("5. Exit")
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
                            print()
                            employeesManager.update_employee_info()
                        case "5":
                            break

                        case _:
                            print("- Invalid inputs")

            case "2":
                while True:
                    print()
                    print(f"-" * 19)
                    print("# Choose an option: ")
                    print(f"-" * 19)
                    print("1. Display Menu")
                    print("2. Add Dish")
                    print("3. Remove Dish")
                    print("4. Update Dish")
                    print("5. Exit")
                    print()
                    option = input("Your choice: ").strip()

                    match option:
                        case "1":
                            menuManager.display_menu()
                        case "2":
                            print()
                            menuManager.load_menu()
                            dishName = input("Enter the dish: ")
                            dishPrice = input("Enter the price: ")
                            print()
                            menuManager.add_dish(dishName, dishPrice)
                        case "3":
                            print()
                            dishName = input("Enter the name of dish to remove: ").strip()
                            print()
                            menuManager.remove_dish(dishName)
                            print()
                        case "4":
                            print()
                            dishName = input("Enter the name of dish to update: ").strip()
                            dishPrice = input("Enter the new price for the dish: ")
                            print()
                            menuManager.update_dish(dishName, dishPrice)
                        case "5":
                            break
                        case _:
                            print("- Invalid inputs")
            
            case "3":
                break
            case _:
                print("- Invalid inputs")






                            


