import shelve
from dataclasses import dataclass
# Working on RPG save system and ways to build class instances a bit more dynamically and finding ways of saving them

# TODO: Steal some pokemon combat stuff and convert it for use here, weakness customization

save = shelve.open("RPG_save")  # Opening the persistent database object
# Currently, I have the main character object's key in the shelve database set to "Protag"


@dataclass()
class Technique:
    name: str  # Name of the attack/technique/move, whatever you want to call it.
    magnitude: int or float  # The magnitude of power, or healing percentage, or amount of buff/debuff in multiples
    cost: int  # Cost to activate the move. (Always in energy? Or maybe ammo for guns, health cost like in Persona 4?)
    target: str  # target possibilities: "Foe/Foes/Self/Ally/Party/All"
    effect: str or list  # Oh, I didn't realize you could do this. Interesting.
    description: str  # Describes what the move does


gram_slice = Technique("Gram Slice", 25, 5, "Foe", "Physical", "Light physical damage to 1 enemy")
bufu = Technique("Bufu", 20, 5, "Foe", "Ice", "Light ice damage to 1 enemy")
zio = Technique("Zio", 20, 5, "Foe", "Lightning", "Light lightning damage to 1 enemy")
zan = Technique("Zan", 20, 5, "Foe", "Wind", "Light wind damage to 1 enemy")
agi = Technique("Agi", 20, 5, "Foe", "Fire", "Light fire damage to 1 enemy")
rapid_needle = Technique("Rapid Needle", 15, 3, "Foes", "Physical", "Light physical damage to all enemies")
tarukaja = Technique("Tarukaja", 1, 8, "Ally", "Attack", "Increase 1 ally's attack power by 1 stage")
rakunda = Technique("Rakunda", -1, 10, "Foe", "Defense", "Decrease 1 enemies defense by 1 stage")
dia = Technique("Dia", 0.33, 7, "Ally", "Health", "Heal one ally for 1/3 of their max health")

technique_list = [gram_slice, tarukaja, rakunda, bufu, zio, zan, agi, rapid_needle, dia]


@dataclass()
class Being:
    name: str
    level: int
    vitality: int
    strength: int
    magic: int
    moves: list
    weaknesses: list

    def __post_init__(self):
        # So these are the full/max values for individual stats
        self.health = self.vitality*7 + self.level*5
        self.energy = self.level*7 + self.vitality*3 + self.magic*2
        self.defense = 100
        self.evasion = 100

        # And these are the active ones that can be altered in battle
        self.act_hp = self.health
        self.act_en = self.energy
        self.act_def = self.defense
        self.act_eva = self.evasion

    # def name_self(self):
    #     #     name = input("What is your name? ")
    #     #     return name


player_walter = Being("Walter", 3, 10, 10, 6, [gram_slice, tarukaja], ["Lightning"])
player_isabeau = Being("Isabeau", 3, 7, 6, 13, [bufu, dia], ["Wind"])
player_jonathan = Being("Jonathan", 3, 9, 8, 9, [zio, rakunda], ["Ice"])
player_custom = Being("Player", 1, 5, 5, 5, [], [])  # Default placeholder for the custom player object

slime = Being("Slime", 1, 4, 6, 6, [agi], ["Lightning", "Fire", "Ice", "Wind"])
rodent = Being("Rodent", 1, 3, 7, 5, [tarukaja, rapid_needle], ["Fire", "Lightning"])
mokoi = Being("Mokoi", 1, 6, 3, 6, [zio], ["Wind"])

encounter_list = [slime, rodent, mokoi]


def divider():
    print("-"*125)


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
    i_v = player.vitality
    i_s = player.strength
    i_m = player.magic

    n = player.name

    distributable_points = 5
    d = distributable_points
    while True:
        v = player.vitality
        s = player.strength
        m = player.magic
        print(f"Player '{n}' stats: Vit - {v, sub(v, i_v)}, Str - {s, sub(s, i_s)}, Mag {m, sub(m, i_m)}")
        print(f"Points left to distribute: {d} (Input h for help)")
        choose_stats = input("Which stat would you like to alter? [vitality - v, strength - s, magic - m]\n").lower()
        if choose_stats == "v" or choose_stats == "vitality":
            sign = input("+ or -:\n").lower()
            if sign == "+" or sign == "add" or sign == "plus":
                player.vitality += 1
                d -= 1
            if sign == "-" or sign == "sub" or sign == "minus":
                player.vitality -= 1
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
        elif choose_stats == "h" or choose_stats == "help":
            print("Vitality affects health and energy, strength is the power of physical attacks")
            print("Magic is the power of magic, effects and has a slight effect on the energy stat")
        if d == 0:
            break_q = input("Distributable points are at zero. Confirm these stat changes? [y/n]").lower()
            if break_q == "y" or break_q == "yes":
                break
            else:
                continue


def choose_move(player):

    ab_count = 2  # Sets the amount of abilities allowed to be chosen from the list

    while True:
        for index, tech in enumerate(technique_list, 1):
            print(f"{index}. {tech.name} | Power: {tech.magnitude} | Cost: {tech.cost} | Effect: {tech.effect}")
        divider()
        print("Please choose two abilities from the above list for your character.")
        ability_choice = input(f"Input the index of the move you want. Choices remaining: {ab_count} \n")
        try:
            num = int(ability_choice)

            if num <= len(technique_list):
                player.moves.append(technique_list[num-1])
                print(f"You have added {technique_list[num-1]} to your move list!")
                ab_count -= 1

            if ab_count == 0:
                print("You have chosen your starting abilities congratulations!")
                break

            if num >= len(technique_list):
                print("This number does not correspond to a value in the list given. Please try again")
                continue

            else:
                continue

        except ValueError:
            print("Not a valid index for the list of options given. Please try again.")
            continue


def player_creation(player):
    self_name(player)
    set_stats(player)
    choose_move(player)
    s = player_custom.strength
    v = player_custom.vitality
    m = player_custom.magic
    print(f"Name: {player.name}, Vit: {v}, Str: {s}, Mag: {m}")
    for tech in player.moves:
        print(tech)
    save["Protag"] = player
    print("Save successful")


def establish_player(player):
    # An adapted version of the tic-tac-toe save system to try to establish player details
    while True:
        try:
            player = save["Protag"]  # Make this something more custom?
            print("Save file detected, player details transferring over...")
            print(player)
            break
        except KeyError:
            print("No save file detected, initiating player creation...")
            player_creation(player)
            break


def general_navigation(player):
    while True:
        decision = input("""You are in town. What would you like to do? 
[1 - Examine self/party, 2 - visit Tavern, 3 - visit Ye Olde Shoppe, 4 - Adventure, 5 - Quit Game] \n""")
        divider()
        if decision == "1":
            print(player)
            continue
        elif decision == "2":
            print("You decided to head to the Tavern.")
            continue
        elif decision == "3":
            print("You decided to visit the General Store")
            continue
        elif decision == "4":
            print("You headed out into the wild to search for a battle.")
            adventure = input("Would you like to battle a wild animal [w] or seek out a dungeon [d]? \n").lower()
            if adventure == "w" or adventure == "wild":
                print("You decided to search the wilderness for some creatures to battle")
            elif adventure == "d" or adventure == "dungeon":
                print("You decided to search the area for a dungeon to explore")
                divider()
            divider()
            continue
        elif decision == "5":
            print("You have chosen to exit the game")
            exit()


def main_game(player):

    establish_player(player)
    divider()
    general_navigation(player)


if __name__ == "__main__":
    main_game(player_custom)
