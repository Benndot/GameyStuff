# Testing to see the interplay between the shelve module and the dependencies of classes from imported files

import shelve
import RPGchar_creation as Rpg
from RPGchar_creation import Player
from RPGchar_creation import Technique

SAVE = shelve.open("RPG_save")

ziodyne = Technique("Ziodyne", 100, 30, ["None"])

d = Player("Test", 5, 10, 8, 12, [Rpg.bufu, Rpg.tarukaja])

print(d)

print(SAVE["Holly"])

d = SAVE["Holly"]

print(d)

SAVE.close()
