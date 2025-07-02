import json
from models.dish import Dish
from tabulate import tabulate
from colorama import init, Fore, Style
init(autoreset=True)

class Cart:
    

    def __init__ (self):
        self.__menu = []
        self.__cart = []

    def load_menu (self):
        try:
            with open("data/menu.json" , "r" , encoding="UTF-8") as file:
                data = json.load(file)
                self.__menu = [Dish.from_dict(item) for item in data]
        except FileNotFoundError:
            self.__menu = []

    def display_menu(self):
        if not self.__menu:
            print("- The menu is empty.")
            return
        else:
            print()
            print(Fore.YELLOW + "     --------- Menu ---------")
            table = []
            for id, dish in enumerate(self.__menu, start=1):
                table.append([id, dish._Dish__name, f"{float(dish._Dish__price):.2f} SR"])
            print(tabulate(table, headers=["No", "Dish Name", "Price"], tablefmt="grid"))




    def add_to_cart(self, choice: int, quantity: int = 1):
        if 1 <= choice <= len(self.__menu):
            selected_dish = self.__menu[choice - 1]
            for i, (d, q) in enumerate(self.__cart):
                if d._Dish__name == selected_dish._Dish__name:
                    self.__cart[i] = (d, q + quantity)
                    print()
                    print(f"- Added {quantity} more of {selected_dish._Dish__name} to the cart.")
                    return
            self.__cart.append((selected_dish, quantity))
            print()
            print(f"- Added {selected_dish._Dish__name} x{quantity} to the cart.")
        


    def remove_from_cart(self, choice: int, quantity: int = 1):
        if 1 <= choice <= len(self.__cart):
            dish, qty = self.__cart[choice - 1]
            if qty > quantity:
                self.__cart[choice - 1] = (dish, qty - quantity)
                print()
                print(f"- Removed {quantity} of {dish._Dish__name}. Remaining: {qty - quantity}")
                print()
            else:
                removed_dish, _ = self.__cart.pop(choice - 1)
                print()
                print(f"- Removed {removed_dish._Dish__name} completely from the cart.")
                print()


    def view_cart(self):
        if not self.__cart:
            print(Fore.RED + "- Your cart is empty.")
            return

        print()
        print(Fore.YELLOW + "                -------- Your Cart --------")
        table_data = []
        total = 0

        for i, (dish, qty) in enumerate(self.__cart, start=1):
            item_total = float(dish._Dish__price) * qty
            total += item_total
            table_data.append([i, dish._Dish__name, f"{dish._Dish__price} SR", qty, f"{item_total:.2f} SR"])

        headers = ["No.", "Name", "Price", "Quantity", "Total"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        print(f"\nTotal: {total:.2f} SR\n")

    

    def clear_cart(self):
        self.__cart = []
        print()
        print("- Cart has been cleared.")
        print()

    def calculate_total(self):
        total = 0
        for dish, qty in self.__cart:
            total += float(dish._Dish__price) * qty
        return total



    def to_dict(self):
        return {
            "cart_items": [
                {
                    "name": dish._Dish__name,
                    "price": dish._Dish__price,
                    "quantity": quantity
                }
                for dish, quantity in self.__cart
            ]
        }

    @staticmethod
    def from_dict(data: dict):
        cart = Cart()
        for item in data.get("cart_items", []):
            dish = Dish(item["name"], item["price"])
            cart._Cart__cart.append((dish, item["quantity"]))
        return cart





    
        
    