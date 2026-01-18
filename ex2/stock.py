from security import *

class Stock(Security):
    def __init__(self, symbol: str, price: float, dividend_yield: float, currency: str = "USD"):
        super().__init__(symbol, price, currency)
        self.dividend_yield = dividend_yield

    def get_expected_dividend(self) -> float:
        return self.price * self.dividend_yield