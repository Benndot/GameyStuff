import shelve


class TestShelve:
    def __init__(self, name, value):
        self.name = name
        self.value = value


if __name__ == "__main__":

    var_save = shelve.open("Num_Save")

    # Default variable values

    w = TestShelve("Zero", 0)

    x = 1

    y = "Two"

    z = [1, 2, 3]

    # Creating shelve variable

    var_save["Wub"] = w

    var_save["Ex"] = x

    var_save["Why"] = y

    var_save["Zee"] = z

    var_save.close()


