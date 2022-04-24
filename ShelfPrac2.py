import shelve
from ShelfPrac import TestShelve

save = shelve.open("Num_Save")

b = save["Wub"]

print(b)

save.close()