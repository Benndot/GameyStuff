import shelve
import RPGchar_creation as Rpg
from RPGchar_creation import Being
from RPGchar_creation import Technique

SAVE = shelve.open("RPG_save")

ziodyne = Technique("Ziodyne", 100, 30, "Foe", "Lightning")

d = Being("Test", 5, 10, 8, 12, [Rpg.bufu, Rpg.tarukaja])

print(d)

print(SAVE["Holly"])

d = SAVE["Holly"]

print(d)

SAVE.close()
