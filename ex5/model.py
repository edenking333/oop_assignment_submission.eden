from typing import List
from person import Person

class Model:
    def __init__(self):
        self._people: List[Person] = []

    def add_person(self, name: str, address: str, phone: str):
        new_person = Person(name, address, phone)
        self._people.append(new_person)
        return new_person

    def get_all_people(self) -> List[Person]:
        return self._people