import json
from models.customer import Customer
from models.cart import Cart
from colorama import init, Fore, Style
init(autoreset=True)

class CustomerManager:
    def __init__ (self):
        self.__customers = []

    def load_customers(self):
        try:
            with open("data/customers.json", "r", encoding="UTF-8") as file:
                data = json.load(file)
                self.__customers = [Customer.from_dict(cust) for cust in data]
        except FileNotFoundError:
            self.__customers = []

    def save_customers(self):
        with open("data/customers.json", "w", encoding="UTF-8") as file:
            data = [customer.to_dict() for customer in self.__customers]
            json.dump(data , file, indent=4)

    def create_or_get_customer (self, phone):
        for cust in self.__customers:
            if cust._Customer__phone == phone:
                print()
                print(Fore.GREEN + "- You're now logged in. Let's start your order!")
                return cust
            
        new_customer = Customer(phone)
        self.__customers.append(new_customer)
        self.save_customers()
        print()
        print(Fore.GREEN + "- New customer registered successfully. Let's start your order!")
        return new_customer
    

    def list_customers(self):
        if not self.__customers:
            print("- No customers registered.")
            return
        for cust in self.__customers:
            print(f"- Phone: {cust._Customer__phone} | Points: {cust._Customer__loyalty_points}")

