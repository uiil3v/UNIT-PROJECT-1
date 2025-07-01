class Dish:
    def __init__ (self, name: str, price: float):
        self.__name = name
        self.__price = price


    def to_dict (self):
        return {
            "name" : self.__name,
            "price" : self.__price
        }
    

    @staticmethod
    def from_dict (data: dict):
        return Dish(
            name = data["name"],
            price = data["price"]
        )