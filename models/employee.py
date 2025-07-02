from tabulate import tabulate

class Employee:
    def __init__ (self , name: str , email: str, phone: str, position: str,  id: str):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__position = position
        self.__id = id
        
    def employeeInfo(self):
        print()
        print("-" *21)
        print("# Employee Information: ")
        print("-" *21)
        print(f"- Name: {self.__name}")
        print(f"- Email: {self.__email}")
        print(f"- Phone: {self.__phone}")
        print(f"- Position: {self.__position}")
        print(f"- ID: {self.__id}")
    
    def to_dict(self):
        return {
            "name" : self.__name,
            "email" : self.__email,
            "phone" : self.__phone,
            "position" : self.__position,
            "id" : self.__id
        }
    
    @staticmethod
    def from_dict(data: dict):
        return Employee(
            name = data["name"], 
            email = data["email"],
            phone = data["phone"],
            position = data["position"],
            id = data["id"]
        )
    

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_position(self):
        return self.__position


