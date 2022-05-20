import random
from dataclasses import dataclass

suit_list = ["Diamonds", "Hearts", "Spades", "Clovers"]


@dataclass()
class Card:
    suit: str
    value: str

    card_dict = {
        "Ace": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Jack": 10,
        "Queen": 11,
        "King": 12,
        "Jester": None
    }

    def print_name(self):
        return f"{self.value} of {self.suit}"


# Heart suit cards
ace_hearts = Card("Hearts", "Ace")
two_hearts = Card("Hearts", "Two")
three_hearts = Card("Hearts", "Three")
four_hearts = Card("Hearts", "Four")
five_hearts = Card("Hearts", "Five")
six_hearts = Card("Hearts", "Six")
seven_hearts = Card("Hearts", "Seven")
eight_hearts = Card("Hearts", "Eight")
nine_hearts = Card("Hearts", "Nine")
jack_hearts = Card("Hearts", "Jack")
queen_hearts = Card("Hearts", "Queen")
king_hearts = Card("Hearts", "King")
jester_hearts = Card("Hearts", "Jester")

# Diamond suit cards
ace_diamonds = Card("Diamonds", "Ace")
two_diamonds = Card("Diamonds", "Two")
three_diamonds = Card("Diamonds", "Three")
four_diamonds = Card("Diamonds", "Four")
five_diamonds = Card("Diamonds", "Five")
six_diamonds = Card("Diamonds", "Six")
seven_diamonds = Card("Diamonds", "Seven")
eight_diamonds = Card("Diamonds", "Eight")
nine_diamonds = Card("Diamonds", "Nine")
jack_diamonds = Card("Diamonds", "Jack")
queen_diamonds = Card("Diamonds", "Queen")
king_diamonds = Card("Diamonds", "King")
jester_diamonds = Card("Diamonds", "Jester")

# Spade suit cards
ace_spades = Card("Spades", "Ace")
two_spades = Card("Spades", "Two")
three_spades = Card("Spades", "Three")
four_spades = Card("Spades", "Four")
five_spades = Card("Spades", "Five")
six_spades = Card("Spades", "Six")
seven_spades = Card("Spades", "Seven")
eight_spades = Card("Spades", "Eight")
nine_spades = Card("Spades", "Nine")
jack_spades = Card("Spades", "Jack")
queen_spades = Card("Spades", "Queen")
king_spades = Card("Spades", "King")
jester_spades = Card("Spades", "Jester")

# Clove suit cards
ace_cloves = Card("Cloves", "Ace")
two_cloves = Card("Cloves", "Two")
three_cloves = Card("Cloves", "Three")
four_cloves = Card("Cloves", "Four")
five_cloves = Card("Cloves", "Five")
six_cloves = Card("Cloves", "Six")
seven_cloves = Card("Cloves", "Seven")
eight_cloves = Card("Cloves", "Eight")
nine_cloves = Card("Cloves", "Nine")
jack_cloves = Card("Cloves", "Jack")
queen_cloves = Card("Cloves", "Queen")
king_cloves = Card("Cloves", "King")
jester_cloves = Card("Cloves", "Jester")

# Tuple of all the different card types
card_types = (ace_hearts, two_hearts, three_hearts, four_hearts, five_hearts, six_hearts, seven_hearts, eight_hearts,
              nine_hearts, jack_hearts, queen_hearts, king_hearts, jester_hearts, ace_diamonds, two_diamonds,
              three_diamonds, four_diamonds, five_diamonds, six_diamonds, seven_diamonds, eight_diamonds, nine_diamonds,
              jack_diamonds, queen_diamonds, king_diamonds, jester_diamonds, ace_spades, two_spades, three_spades,
              four_spades, five_spades, six_spades, seven_spades, eight_spades, nine_spades, jack_spades, queen_spades,
              king_spades, jester_spades, ace_cloves, two_cloves, three_cloves, four_cloves, five_cloves, six_cloves,
              seven_cloves, eight_cloves, nine_cloves, jack_cloves, queen_cloves, king_cloves, jester_cloves)

# List of the general deck used in most traditional playing card games
general_deck = [ace_hearts, two_hearts, three_hearts, four_hearts, five_hearts, six_hearts, seven_hearts, eight_hearts,
                nine_hearts, jack_hearts, queen_hearts, king_hearts, ace_diamonds, two_diamonds, three_diamonds,
                four_diamonds, five_diamonds, six_diamonds, seven_diamonds, eight_diamonds, nine_diamonds,
                jack_diamonds, queen_diamonds, king_diamonds, ace_spades, two_spades, three_spades, four_spades,
                five_spades, six_spades, seven_spades, eight_spades, nine_spades, jack_spades, queen_spades,
                king_spades, ace_cloves, two_cloves, three_cloves, four_cloves, five_cloves, six_cloves, seven_cloves,
                eight_cloves, nine_cloves, jack_cloves, queen_cloves, king_cloves]

for card in card_types:
    print(card.print_name(), Card.card_dict.get(card.value))


@dataclass()
class CardGame:
    deck: list
    hand: list
    hand_size: int

    def draw(self):
        if len(self.deck) == 0:
            print("Empty deck")
        else:
            drawn_card = random.choice(self.deck)
            print(drawn_card)
            self.deck.remove(drawn_card)
            self.hand.append(drawn_card)

    def view_hand(self):
        for cards in self.hand:
            print(cards.print_name())


test_game = CardGame(general_deck, [], 5)
print(len(test_game.deck))
test_game.draw()
test_game.draw()
print(test_game.view_hand())
print(len(test_game.deck))
