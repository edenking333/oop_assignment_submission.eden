class View:
    def show_menu(self):
        print("\n--- MVC Contact Manager ---")
        print("1. Add Person")
        print("2. Show All People")
        print("3. Exit")
    
    def get_input(self, prompt):
        return input(f"{prompt}: ").strip()

    def display_message(self, message):
        print(f"📢 {message}")

    def display_list(self, items):
        print("\n--- Contact List ---")
        if not items:
            print("No contacts found.")
        for item in items:
            print(item)