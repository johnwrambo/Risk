from RuleBook import game_data
import random


class RiskCard:
    """Creates Risk Cards to be owned by the RiskDeck"""

    def __init__(self, color: str, territory: str, suits: str, symbol: str, continent: str = None):
        self.territory = territory
        self.suit = suits
        self.symbol = game_data.suit_symbols[symbol]
        self.color = color
        self.continent = continent

    def __str__(self):
        """
        Creates a viusal display of the cards
        :param cards:
        :return: None
        """
        return f"{game_data.colors["bg_color"]["black"]}{game_data.colors["text_color"][self.color]}|{self.territory.title().replace("_", " ")} {self.symbol}|{game_data.colors["text_color"]["reset"]}"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return 1


class RiskDeck:

    def __init__(self):
        self._build_deck()
        self._create_wild_cards()
        self.discard_pile = []

    def _build_deck(self):
        territory_list = [territory for territory in game_data.territories.keys()]
        cards = []
        for territory_name in territory_list:
            continent = game_data.territories[territory_name]["continent"]
            color = game_data.continents[continent]["color"]
            continent = game_data.territories[territory_name]
            suit = game_data.territories[territory_name]["card_suit"]
            card_object = RiskCard(color, territory_name, suit, suit, continent)
            cards.append(card_object)
            setattr(self, "cards", cards)
            setattr(self, "discard_pile", [])
        return self

    def _create_wild_cards(self):
        wild_cards = []
        wild_card1 = RiskCard("white", "Wild Card", "wild", "wild", "None")
        wild_card2 = RiskCard("white", "Wild Card", "wild", "wild", "None")
        wild_cards.append(wild_card1)
        wild_cards.append(wild_card2)
        setattr(self, "wild_cards", wild_cards)

    def insert_wild_card(self):
        self.cards.extend(self.wild_cards)
        return self

    def discard(self,cards):
        discard_cards = cards
        cards = len(discard_cards)
        for _ in range(cards):
            deck.discard_pile.append(discard_cards.pop())
        return self
    def reintegrate_discard(self):
        self.cards.extend(self.discard_pile)
        self.shuffle_deck()
        self.split_deck()
        return self

    def shuffle_deck(self):
        shuffled_cards = []
        number_cards = len(self.cards)
        for n in range(0, number_cards):
            shuffled_cards.append(self.cards.pop(random.randint(0, len(self.cards) - 1)))
        self.cards = shuffled_cards
        return self


    def split_deck(self):
        middle = int(len(self.cards) / 2)
        variation = int(len(self.cards) * .1 / 2)
        middle_low = middle - variation
        middle_high = middle + variation
        middle = random.randint(middle_low, middle_high)
        split_deck_1 = self.cards[:middle]
        split_deck_2 = self.cards[middle:]
        self.cards = split_deck_2 + split_deck_1
        return self

    def deal_card(self):
        dealt_card = self.cards.pop(0)
        return dealt_card

    def deal_cards(self, number_cards: int):
        dealt_cards = []
        for _ in range(number_cards):
            dealt_cards.append(self.deal_card())
        return dealt_cards

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        for card in self.cards:
            yield card

    def __str__(self):
        deck_string = ""
        for n, card in enumerate(self.cards):
            if (n + 1) % 5 == 0:
                deck_string += str(card) + "\n"
            else:
                deck_string += str(card) + " "

        deck_string = deck_string + "\n"
        return deck_string

    def __repr__(self):
        deck_size = len(self.cards)
        deck_string = ""
        for card in self.cards:
            deck_string += str(card)
        deck_string = f" {deck_size} Cards\n{deck_string} + \n"
        return deck_string


class PlayerDeck(RiskDeck):

    def __init__(self):
        self.cards = []

    def append(self,input):
        self.cards.append(input)
        return self

deck = RiskDeck()
# print(deck.cards)

