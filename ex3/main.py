from dog import Dog
from cat import Cat
from duck import Duck
from zoo_chorus import ZooChorus

if __name__ == "__main__":
    zoo = [Dog(), Cat(), Duck()]
    chorus = ZooChorus()
    chorus.sing(zoo)