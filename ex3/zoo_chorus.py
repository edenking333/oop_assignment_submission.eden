from animal import *

class ZooChorus:
    def sing(self, animals_list: list):
        print("--- The Zoo Chorus ---")
        for animal in animals_list:
            if isinstance(animal, Animal):
                print(f"{type(animal).__name__} says: {animal.speak()}")
            else:
                print("Unknown creature!")