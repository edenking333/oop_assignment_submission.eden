class Invoice:
    def __init__(self, inv_id: int, client: str, amount: float, date: str):
        self._inv_id = inv_id
        self._client = client
        self.__amount = amount
        self._date = date
        self._is_paid = False

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, value: float):
        if value < 0:
            raise ValueError("Amount cannot be negative!")
        self.__amount = value

    @property
    def client(self) -> str:
        return self._client

    @client.setter
    def client(self, name: str):
        if not name or len(name.strip()) == 0:
            raise ValueError("Client name cannot be empty.")
        self._client = name

    def mark_as_paid(self):
        self._is_paid = True

    def get_summary(self) -> str:
        status = "PAID" if self._is_paid else "OPEN"
        return f"[Invoice #{self._inv_id}] Client: {self.client}, Amount: {self.amount}$, Status: {status}"