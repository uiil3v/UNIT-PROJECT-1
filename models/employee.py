

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
    

    def update_employee_info(self):
        while True:
            print()
            print("Which information do you want to update?")
            print("1. Name")
            print("2. Email")
            print("3. Phone")
            print("4. Position")
            print("5. ID")
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
                    new_position = input("Enter the new position: ")
                    self.__position = new_position
                case "5":
                    new_id = input("Enter the new ID: ").strip()
                    if new_id.isdigit():
                        self.__id = new_id
                    print(f"ID changed to {new_id} successfully.")
                case "6":
                    break
                case _:
                    print("Invalid input.")
    


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


