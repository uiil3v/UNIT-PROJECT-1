from models.dish import Dish
import json

class Menu:


    def __init__(self):
        self.__menu = []

    def add_dish(self, name: str, price: float):
        for dish in self.__menu:
            if dish._Dish__name == name:
                print("- This dish already exist!")
                return
        self.__menu.append(Dish(name, price))
        print(f"- '{name}' has been added to the menu for {price} SR.")
        self.save_menu()
    
    def remove_dish (self, name: str):
        for dish in self.__menu:
            if dish._Dish__name == name:
                self.__menu.remove(dish)
                print(f"- '{name}' has been removed successfully.")
                self.save_menu()
                return
        print(f"- The dish '{name}' does not exist!")

    def update_dish (self, name: str, new_price):
        for dish in self.__menu:
            if dish._Dish__name == name:
                dish._Dish__price = new_price
                print(f"- '{name}' has been updated successfully.")
                self.save_menu()
                return
        print(f"- The dish '{name}' does not exist!")


    def display_menu(self):
        if not self.__menu:
            print("- The menu is empty.")
        else:
            print()
            print("------- Menu -------")
            print()
            for dish in self.__menu:
                print(f"{dish._Dish__name}: {dish._Dish__price} SR")
            print()

    
    def load_menu (self):
        try:
            with open("data/menu.json" , "r" , encoding="UTF-8") as file:
                data = json.load(file)
                self.__menu = [Dish.from_dict(item) for item in data]
        except FileNotFoundError:
            self.__menu = []

    def save_menu (self):
            with open("data/menu.json" , "w" , encoding="UTF-8") as file:
                data = [dish.to_dict() for dish in self.__menu]
                json.dump(data , file , indent=4)
    
                      