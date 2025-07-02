from managers.manager import Manager
from models.employee import Employee
from managers.menu import Menu
from managers.customerManager import CustomerManager
from models.cart import Cart
from models.customer import Customer
from tabulate import tabulate
from colorama import init, Fore, Style
init(autoreset=True)


while True:
    print()
    print(Fore.BLUE + "--- Welcome to Burgerly Restaurant ---")
    print("1. Login as Manager")
    print("2. Continue as Customer")
    print("3. Exit")

    option = input(Fore.GREEN + "Your choice: ").strip()

    match option:
        case "1":
            manager = Manager()
            manager.load_managers()

            logged_in = False
            logged_manager = None
            while True:
                print()
                print(Fore.BLUE + "***** SIGN IN *****")
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
                    print(Fore.RED + "- Wrong username or password. Please try again.")
                

            employeesManager = Manager()
            employeesManager.load_employees()
            menuManager = Menu()
            menuManager.load_menu()

            if logged_in:

                while True:
                    print()
                    print(Fore.YELLOW + f"- Welcome {logged_manager._ManagerAccount__name}!")
                    print()
                    print(Fore.LIGHTBLUE_EX + f"-" * 19)
                    print(Fore.BLUE + "# Choose an option: ")
                    print(Fore.LIGHTBLUE_EX + f"-" * 19)
                    print("1. Employee Settings")
                    print("2. Menu Settings")
                    print("3. Exit")
                    print()
                    
                    option = input(Fore.GREEN + "Your choice: ").strip()

                    match option:
                        case "1":

                            while True:
                                print()
                                print(Fore.LIGHTBLUE_EX + f"-" * 19)
                                print(Fore.BLUE + "# Choose an option: ")
                                print(Fore.LIGHTBLUE_EX + f"-" * 19)
                                print("1. List Employees")
                                print("2. Add Employee")
                                print("3. Remove Employee")
                                print("4. Update Employee Information")
                                print("5. Exit")
                                print()
                                option = input(Fore.GREEN + "Your choice: ").strip()

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
                                            print()
                                            print(Fore.RED + "- The ID must be a number.")
                                        print()
                                    case "4":
                                        print()
                                        employeesManager.update_employee_info()
                                    case "5":
                                        break

                                    case _:
                                        print(Fore.RED + "- Invalid inputs")

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
                                option = input(Fore.GREEN + "Your choice: ").strip()

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
                                        print(Fore.RED + "- Invalid inputs")
                        
                        case "3":
                            break
                        case _:
                            print()
                            print(Fore.RED + "- Invalid inputs")


        case "2":
            cust = CustomerManager()
            cust.load_customers()

            print()
            print(Fore.BLUE + "***** CUSTOMER LOGIN *****")
            while True:
                phone = input("Enter your phone number: ").strip()
                if phone.isdigit():
                    custClass = cust.create_or_get_customer(phone)
                    custClass._Customer__cart.load_menu()
                    break
                else:
                    print()
                    print(Fore.RED + "- Invalid input. Please enter digits only.")
                    print()
            while True:
                print()
                print(Fore.LIGHTBLUE_EX + f"-" * 19)
                print(Fore.BLUE + "# Choose an option: ")
                print(Fore.LIGHTBLUE_EX + f"-" * 19)
                print("1. View Menu")
                print("2. Add to Cart")
                print("3. Remove from or Clear Cart")
                print("4. View Cart")
                print("5. Place Order ")
                print("6. Redeem Loyalty Points")
                print("7. View Loyalty Info")
                print("8. Exit")
                print()

                option = input("Enter Your choice: ").strip()
                print()

                match option:
                    case "1":
                        custClass._Customer__cart.display_menu()
                    case "2":
                            while True:
                                choice = input("Enter the meal number(or 0 to stop): ").strip()
                                if choice == "0":
                                    break
                                quantity = input("Enter the quantity you want: ").strip()
                                if choice.isdigit() and quantity.isdigit():
                                    custClass._Customer__cart.add_to_cart(int(choice), int(quantity))
                                    print()
                                else:
                                    print()
                                    print(Fore.RED + "- Only numbers, please.")
                                    print()
                    case "3":
                        while True:
                            print("Choose what you want:")
                            print("0. Back to Main Menu")
                            print("1. Clear Cart")
                            print("2. Remove from Cart")
                            print()

                            option = input(Fore.GREEN + "Enter Your choice: ").strip()
                            if option.isdigit() :
                                match option:
                                    case "0":
                                        break
                                    case "1":
                                        custClass._Customer__cart.clear_cart()
                                    case "2":
                                        print()
                                        custClass._Customer__cart.view_cart()
                                        choice = input("Enter the meal number: ").strip()
                                        quantity = input("Enter the quantity you want: ").strip()

                                        if choice.isdigit() and quantity.isdigit():
                                            custClass._Customer__cart.remove_from_cart(int(choice), int(quantity))
                                        else:
                                            print()
                                            print(Fore.RED + "- Only numbers, please.")
                                            print()             
                            else:
                                print()
                                print(Fore.RED + "- Only numbers, please.")
                                print()
                    case "4":
                        custClass._Customer__cart.view_cart()
                    case "5":
                        confirm = input("Are you sure you want to place the order? (y/n): ").lower().strip()
                        if confirm == 'y':
                            total = custClass.place_order()
                            points_earned = int(total // 10)  
                            custClass.update_loyalty_points(points_earned)
                            cust.save_customers()

                            print()
                            print(f"- Order placed successfully! Total: {total:.2f} SR")
                            print(f"- You earned {points_earned} loyalty points.")
                            print(f"- Your current status: {custClass.customer_info()['membership_level']}")
                        else:
                            print()
                            print(Fore.RED + "- Order cancelled.")                
                    case "6":
                        if custClass.customer_info()["loyalty_points"] > 0:
                            custClass.redeem_points()
                            cust.save_customers()
                            print("- Your points have been successfully redeemed.")
                        else:
                            print("- You don't have any loyalty points to redeem.")
                    case "7":
                        custClass.check_loyalty_status()
                        info = custClass.customer_info()
                        print()
                        print(Fore.YELLOW + "------ Loyalty Info ------")
                        print(f"Phone Number     : {info['phone']}")
                        print(f"Loyalty Points   : {info['loyalty_points']}")
                        print(f"Membership Level : {info['membership_level']}")
                        print()
                    case "8":
                        break
                    case _:
                        print(Fore.RED + "- Invalid inputs.")


        case "3":
            break
        case _:
            print()
            print(Fore.RED + "- Invalid inputs.")
            







                            


