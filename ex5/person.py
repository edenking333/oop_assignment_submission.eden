from dataclasses import dataclass

@dataclass
class Person:
    name: str
    address: str
    phone: str

    def __str__(self):
        return f" name : {self.name} | self address :{self.address} | self phone: {self.phone}"