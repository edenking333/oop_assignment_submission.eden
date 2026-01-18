from invoice import *

class InvoiceManager:
    def create_and_test(self):
        try:
            print("--- Creating Invoice ---")
            inv = Invoice(101, "Google Inc", 5000.0, "2026-01-14")
            print(f"Initial: {inv.get_summary()}")
            
            print("Updating amount...")
            inv.amount = 6000.0
            inv.mark_as_paid()
            print(f"Final: {inv.get_summary()}")
            
        except ValueError as e:
            print(f"Error: {e}")