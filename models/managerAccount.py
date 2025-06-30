class ManagerAccount:
    

    def __init__ (self, name: str, email: str, phone: str, username: str, password: str):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__username = username
        self.__password = password

    

    def to_dict(self):
        return {
            "name" : self.__name,
            "email" : self.__email,
            "phone" : self.__phone,
            "username" : self.__username,
            "password" : self.__password
        }
    
    @staticmethod
    def from_dict(data: dict):
        return ManagerAccount(
            name = data["name"],
            email = data["email"],
            phone = data["phone"],
            username = data["username"],
            password = data["password"]
        )