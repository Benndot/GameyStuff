import shelve
# Working on RPG save system and ways to build class instances a bit more dynamically and finding ways of saving them

save = shelve.open("RPG_save")


class Player:
    def __init__(self, name, health, strength, magic, moves):
        self.name = name
        self.base_health = health
        self.strength = strength
        self.magic = magic
        self.moves = moves

        # Do active stats

    # def name_self(self):
    #     #     name = input("What is your name? ")
    #     #     return name


class Move:
    def __init__(self, name, power, cost, effect):
        self.name = name
        self.power = power
        self.cost = cost
        self.effect = effect


player_flynn = Player("Flynn", 10, 10, 8, [])
player_isabeau = Player("Isabeau", 7, 6, 13, [])
player_custom = Player("Player", 5, 5, 5, [])


def sub(value1, value2):
    result = int(value1) - int(value2)
    if result == 0:
        return ""
    else:
        return f"(+{result})"


def self_name(player):  # Should this be a class function?
    while True:
        name_self = input("What would you like to name yourself? ").title()
        if 1 > len(name_self) > 25:
            print("Please choose a name between 1 and 25 characters long")
            continue
        else:
            confirm = input(f"Are you sure you want your name to be {name_self}? [Yes/No] ").lower()
            if confirm == "yes" or confirm == "yup" or confirm == "yee" or confirm == "affirmative" or confirm == "y":
                player.name = name_self
                break
            elif confirm == "no" or confirm == "nah" or confirm == "negative" or confirm == "nope" or confirm == "n":
                continue


def set_stats(player):
    # Need to limit subtractions below init values

    # Initial stats before increase distribution takes place
    i_h = player.base_health
    i_s = player.strength
    i_m = player.magic

    n = player.name

    distributable_points = 5
    d = distributable_points
    while True:
        h = player.base_health
        s = player.strength
        m = player.magic
        print(f"Player '{n}' stats: Health - {h, sub(h, i_h)}, Str - {s, sub(s, i_s)}, Mag {m, sub(m, i_m)}")
        print(f"Points left to distribute: {d}")
        choose_stats = input("Which stat would you like to alter? [base_health - h, strength - s, magic - m]\n").lower()
        if choose_stats == "h" or choose_stats == "base_health":
            sign = input("+ or -:\n").lower()
            if sign == "+" or sign == "add" or sign == "plus":
                player.base_health += 1
                d -= 1
            if sign == "-" or sign == "sub" or sign == "minus":
                player.base_health -= 1
                d += 1
        elif choose_stats == "s" or choose_stats == "strength":
            sign = input("+ or -:\n").lower()
            if sign == "+" or sign == "add" or sign == "plus":
                player.strength += 1
                d -= 1
            if sign == "-" or sign == "sub" or sign == "minus":
                player.strength -= 1
                d += 1
        elif choose_stats == "m" or choose_stats == "magic":
            sign = input("+ or -:\n").lower()
            if sign == "+" or sign == "add" or sign == "plus":
                player.magic += 1
                d -= 1
            if sign == "-" or sign == "sub" or sign == "minus":
                player.magic -= 1
                d += 1
        if d == 0:
            break_q = input("Distributable points are at zero. Confirm these stat changes? [y/n]").lower()
            if break_q == "y" or break_q == "yes":
                break
            else:
                continue


def establish_player(player):
    # An adapted version of the tic-tac-toe save system to try to establish player details
    while True:
        try:
            save[player.name]
        except KeyError:
            print("Save file not found, player given default details instead")
            return player_flynn


# establish_player(player_flynn)

self_name(player_custom)
set_stats(player_custom)
print(player_custom.base_health, player_custom.strength, player_custom.magic)
