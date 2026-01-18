from security import Security

class Option(Security):
    def __init__(self, symbol: str, price: float, strike_price: float, expiry_date: str, currency: str = "USD"):
        super().__init__(symbol, price, currency)
        self.strike_price = strike_price
        self.expiry_date = expiry_date

    def calculate_intrinsic_value(self, current_market_price: float) -> float:
        if current_market_price > self.strike_price:
            return current_market_price - self.strike_price
        return 0.0