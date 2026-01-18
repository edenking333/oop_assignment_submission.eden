from security import *

class Bond(Security):
    def __init__(self, symbol: str, price: float, interest_rate: float, years: int, currency: str = "USD"):
        super().__init__(symbol, price, currency)
        self.interest_rate = interest_rate
        self.years = years

    def calculate_maturity_value(self) -> float:
        return self.price * ((1 + self.interest_rate) ** self.years)