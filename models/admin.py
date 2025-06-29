from menu import Menu

class Admin:
    def __init__ (self , name: str , email: str, phone: str, username: str, password: str):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__username = username
        self.__password = password
        self.menu = Menu

    def login (self, username: str, password: str):
        if self.username == username and self.password == password:
            return f"Login successfully. Welcome, {self.name}."
        else:
            return f"Invalid username or password!"
        
    def adminInfo(self):
        print()
        print("-" *21)
        print("# Admin Information: ")
        print("-" *21)
        print(f"- Name: {self.__name}")
        print(f"- Email: {self.__email}")
        print(f"- Phone: {self.__phone}")
        print(f"- Username: {self.__username}")
        print(f"- Password: {self.__password}")
    

    def update_admin_info(self):
        while True:
            print()
            print("Which information do you want to update?")
            print("1. Name")
            print("2. Email")
            print("3. Phone")
            print("4. Username")
            print("5. Password")
            print("6. Exit")
            print()

            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    new_name = input("Enter the new name: ")
                    self.__name = new_name
                    print(f"Name changed to {new_name} successfully.")
                case "2":
                    new_email = input("Enter the new email(@gmail, @hotmail, or @outlook): ").lower().strip()
                    if new_email.endswith(("@gmail.com", "@hotmail.com" , "@outlook.com")):
                        self.__email = new_email
                        print(f"Email changed to {new_email} successfully.")
                    else:
                        print("Invalid email domain.")
                case "3":
                    new_phone = input("Enter the new phone(05********): ")
                    if new_phone.startswith("05") and new_phone.isdigit() and len(new_phone) == 10:
                        self.__phone = new_phone
                        print(f"Phone changed to {new_phone} successfully.")
                    else:
                        print("Invalid phone number.")
                case "4":
                    new_username = input("Enter the new username: ").lower().strip()
                    self.__username = new_username
                    print(f"Username changed to {new_username} successfully.")
                case "5":
                    new_password = input("Enter the new password: ").strip()
                    self.__password = new_password
                    print(f"Password changed to {new_password} successfully.")
                case "6":
                    break
                case _:
                    print("Invalid input.")
    

    def add_dish(self, dish: str, price: float):
        self.menu.add_dish(dish, price)

    def remove_dish (self, dish: str):
        self.menu.remove_dish(dish)

    def update_dish (self, dish: str, new_price: float):
        self.menu.update_dish(dish, new_price)

    def display_menu(self):
        self.menu.display_menu()

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
        return Admin(
            name = data["name"], 
            email = data["email"],
            phone = data["phone"],
            username = data["username"],
            password = data["password"]
        )


