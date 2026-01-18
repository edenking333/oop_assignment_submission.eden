class Security:
    def __init__(self, symbol: str, price: float, currency: str = "USD"):
        self.symbol = symbol
        self.price = price
        self.currency = currency

    def get_base_info(self) -> str:
        return f"{self.symbol}: {self.price} {self.currency}"