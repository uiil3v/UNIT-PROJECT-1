from models.menu import Menu

menu1 = Menu()

while True:

    print("-" *10)
    print("# Options: ")
    print("1. Add a dish.")
    print("2. Remove a dish.")
    print("3. Display menu.")
    print("4. Exit.")
    print("-" *10)
    print()

    option = input("choose what you want? ")

    match option:
        case "1":
            dish = input("Enter a dish to add: ")
            price = float(input("Enter a price: "))
            menu1.add_dish(dish , price)
        
        case "2":
              dish = input("Enter a dish to remove: ")
              menu1.remove_dish(dish)

        case "3":
              menu1.display_menu()
        
        case "4":
              print("Thank you for using our program.")
              break
         
        case _:
              print("Invalid input.")
            

    

