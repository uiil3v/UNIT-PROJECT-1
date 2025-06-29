class Menu:


    def __init__(self):
        self.dishes = {}

    def add_dish(self, dish: str, price: float):
        if dish in self.dishes:
            print(f"This dish already exists!")
        else:
            self.dishes[dish] = price
            print(f"'{dish}' has been added to the menu for {price} SR.")
    
    def remove_dish (self, dish: str):
        if dish in self.dishes:
            del self.dishes[dish]
            print(f"'{dish}' has been removed successfully.")
        else:
            print(f"The dish '{dish}' does not exist!")

    def update_dish (self, dish: str, new_price: float):
        if dish in self.dishes:
            self.dishes[dish] = new_price
            print(f"'{dish}' has been updated successfully.")
        else:
            print(f"The dish '{dish}' does not exist!")

    def display_menu(self):
        if not self.dishes:
            print("The menu is empty.")
        else:
            print()
            print("---Menu---")
            print()
            for dish, price in self.dishes.items():
                print(f"{dish}: {price} SR")
            print()
                      