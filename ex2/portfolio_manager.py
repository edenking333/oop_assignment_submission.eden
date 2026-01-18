from stock import Stock
from bond import Bond
from option import Option

class PortfolioManager:
    def run_simulation(self):
        print("--- Securities Simulation ---")
        
        apple = Stock("AAPL", 180, 0.05)
        print(f"Stock: {apple.get_base_info()} | Dividend: {apple.get_expected_dividend()}$")
        
        bond = Bond("US-10Y", 1000, 0.03, 10)
        print(f"Bond: {bond.get_base_info()} | Maturity Value: {bond.calculate_maturity_value():.2f}$")
        
        opt = Option("AAPL-CALL", 5.0, 190.0, "2025-27-12")
        print(f"Option: {opt.get_base_info()} | Value at 200$: {opt.calculate_intrinsic_value(200.0)}$")