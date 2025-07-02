from models.dish import Dish
import json
from tabulate import tabulate
from colorama import init, Fore, Style
init(autoreset=True)

class Menu:


    def __init__(self):
        self.__menu = []

    def add_dish(self, name: str, price: float):
        for dish in self.__menu:
            if dish._Dish__name == name:
                print(Fore.RED + "- This dish already exist!")
                return
        self.__menu.append(Dish(name, price))
        print(Fore.GREEN + f"- '{name}' has been added to the menu for {price} SR.")
        self.save_menu()
    
    def remove_dish (self, name: str):
        for dish in self.__menu:
            if dish._Dish__name == name:
                self.__menu.remove(dish)
                print(Fore.GREEN + f"- '{name}' has been removed successfully.")
                self.save_menu()
                return
        print(Fore.RED + f"- The dish '{name}' does not exist!")

    def update_dish (self, name: str, new_price):
        for dish in self.__menu:
            if dish._Dish__name == name:
                dish._Dish__price = new_price
                print(Fore.GREEN + f"- '{name}' has been updated successfully.")
                self.save_menu()
                return
        print(Fore.RED + f"- The dish '{name}' does not exist!")


    def display_menu(self):
        if not self.__menu:
            print(Fore.RED + "- The menu is empty.")
            return
        else:
            print()
            print(Fore.YELLOW + "   --------- Menu ---------")
            table = []
            for dish in self.__menu:
                table.append([dish._Dish__name, f"{float(dish._Dish__price):.2f} SR"])
            print(tabulate(table, headers=["Dish Name", "Price"], tablefmt="grid"))

    
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
    
                      