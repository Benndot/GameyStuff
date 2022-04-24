import shelve
import RPGchar_creation as Rpg
from RPGchar_creation import Being
from RPGchar_creation import Technique

SAVE = shelve.open("RPG_save")

ziodyne = Technique("Ziodyne", 100, 30, "Foe", "Lightning", "Deal heavy lightning damage to 1 enemy")

d = Being("Test", 5, 10, 8, 12, [Rpg.bufu, Rpg.tarukaja], ["Fire"])

print(d)

print(SAVE["Holly"])

d = SAVE["Holly"]

print(d)

SAVE.close()
