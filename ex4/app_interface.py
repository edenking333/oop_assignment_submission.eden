from math_logic import MathLogic

class AppInterface:
    def __init__(self):
        self.logic = MathLogic()

    def run(self):
        print("--- Modular Math Checker (Type -1 to exit) ---")
        while True:
            try:
                user_input = input("Enter two numbers (e.g., '10 5'): ")
                if user_input.strip() == "-1":
                    print("Goodbye!")
                    break
                
                parts = list(map(int, user_input.split()))
                if len(parts) != 2:
                    print("Please enter exactly two numbers.")
                    continue
                    
                n1, n2 = parts
                if self.logic.is_multiple(n1, n2):
                    print(f"✅ Yes! {max(n1, n2)} is a multiple of {min(n1, n2)}")
                else:
                    print("❌ No connection found.")
                    
            except ValueError:
                print("Invalid input. Please enter numbers only.")
