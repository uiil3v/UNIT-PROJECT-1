import json
from models.cart import Cart

class Customer:

    def __init__ (self, phone: str):
        self.__phone = phone
        self.__loyalty_points = 0
        self.__membership_level = None
        self.__cart = Cart()
        self.__order_history = []


    def customer_info (self):
        return {
            "phone" : self.__phone,
            "loyalty_points" : self.__loyalty_points,
            "membership_level" : self.__membership_level
        }
    
    def update_loyalty_points (self, points: int):
        self.__loyalty_points += points

    def redeem_points(self):
        self.__loyalty_points = 0

    def check_loyalty_status (self):
        if self.__loyalty_points >= 100:
            self.__membership_level = "Gold"
        elif self.__loyalty_points >= 50:
            self.__membership_level = "Silver"
        else:
            self.__membership_level = "Bronze"

    def place_order(self):
        total = self.__cart.calculate_total()
        self.__order_history.append(self.__cart)
        earned_points = int(total)
        self.update_loyalty_points(earned_points)
        self.__cart = Cart() 
        self.check_loyalty_status()
        return total
    
    def to_dict(self):
        return {
            "phone" : self.__phone,
            "loyalty_points" : self.__loyalty_points,
            "membership_level" : self.__membership_level,
            "order_history" :[cart.to_dict() for cart in self.__order_history]
        }
    
    @staticmethod
    def from_dict(data: dict):
        customer = Customer(data["phone"])
        customer.__loyalty_points = data["loyalty_points"]
        customer.__membership_level = data["membership_level"]
        customer.__order_history = [Cart.from_dict(cart_data)
            for cart_data in data["order_history"]]
        return customer


