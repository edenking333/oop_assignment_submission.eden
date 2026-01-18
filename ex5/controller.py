from model import *
from view import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_input("Choose option")

            if choice == "1":
                self._handle_add_person()
            elif choice == "2":
                self._handle_show_all()
            elif choice == "3":
                self.view.display_message("Exiting...")
                break
            else:
                self.view.display_message("Invalid option!")

    def _handle_add_person(self):
        name = self.view.get_input("Enter Name")
        address = self.view.get_input("Enter Address")
        phone = self.view.get_input("Enter Phone")
        
        if name and phone:
            self.model.add_person(name, address, phone)
            self.view.display_message(f"User {name} added successfully!")
        else:
            self.view.display_message("Name and Phone are required!")

    def _handle_show_all(self):
        people = self.model.get_all_people()
        self.view.display_list(people)