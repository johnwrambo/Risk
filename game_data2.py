import pandas as pd
import random
import math


def compare_dice(attacker, defender):
    attacker_losses = []
    defender_losses = []
    for i in range(3):
        if not (attacker[i] == 0 or defender[i] == 0):
            if attacker[i] == defender[i]:
                attacker_losses.append(1)
            elif attacker[i] < defender[i]:
                attacker_losses.append(1)
            elif attacker[i] > defender[i]:
                defender_losses.append(1)

    print(attacker_losses)
    print(defender_losses)
    return sum(attacker_losses), sum(defender_losses)


class Territory:
    """Class that defines a territory within the GameEngine class."""

    def __init__(self, territory_data: pd.Series):
        self.name = territory_data["name"]
        self.continent = territory_data["continent"]
        self.continent_color = territory_data["continent_color"]
        self.connections = self.init_connections(territory_data)
        self.garrison = []
        self.occupied_by = territory_data["occupied_by"]
        self.card_suit = territory_data["card_suit"]

    def __str__(self):
        return self.name.replace("_", " ").title()

    def __repr__(self):
        return f"[{self.name}, {self.continent.replace("_", " ").title()}]"

    def garrison_troops(self, brigade):
        self.garrison = brigade

    def init_connections(self, territory_data):
        connection_list = territory_data["connections"].split(",")
        for n, connected in enumerate(connection_list):
            connection_list[n] = connected.strip().replace(" ", "_")
        return connection_list

    # def occupy(self):


def get_colors():
    text_colors = {
        "reset": "\033[0m",
        "black": "\033[30m",
        "red": "\033[38;2;255;0;0m",
        "red1": "\033[91m",
        "light_red": "\033[1;31m",
        "blue": "\033[38;2;0;0;255m",
        "green": "\033[38;2;0;105;0m",
        "yellow": "\033[33m",
        "orange": "\033[38;5;208m",
        "purple": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[38;2;255;255;255m",
        "gray": "\033[90m",
        "light_gray": "\033[37m",
        "magenta": "\033[95m",
        "bright_green": "\033[92m"
    }

    bg_colors = {
        "black": "\033[48;2;0;0;0m",
        "white": "\033[48;2;255;255;255m",
        "gray": "\033[48;2;155;155;155m",
        "red": "\033[48;2;255;0;0m",
        "blue": "\033[48;2;0;0;255m",
        "green": "\033[48;2;0;105;0m",
        "yellow": "\033[48;2;255;255;0m",
        "orange": "\033[48;5;208m",
        "purple": "\033[48;2;128;0;128m",
        "cyan": "\033[48;2;0;255;255m",
        "light_gray": "\033[48;5;250m",
        "dark_gray": "\033[48;5;235m"
    }

    colors = {"text_color": text_colors, "bg_color": bg_colors}
    return colors


def get_emojis():
    emojis = {
        "santa": "🎅",
        "detective": "🕵️",
        "wizard": "🧙‍♂️",
        "vampire": "🧛‍♂️",
        "zombie": "🧟‍♂️",
        "genie": "🧞",
        "fairy": "🧚",
        "elf": "🧝",
        "brain": "🧠",
        "superhero": "🦸‍♂️",
        "super_villain": "🦹‍♂️",
        "merman": "🧜‍♂️",
        "astronaut": "👨‍🚀",

        "airplane": "✈️",
        "helicopter": "🚁",
        "rocket": "🚀",
        "ufo": "🛸",
        "boat": "🛥️",
        "police_car": "🚔",
        "takeoff": "🛫",
        "landing": "🛬",

        "dragon": "🐉",
        "dragon_head": "🐲",
        "snake": "🐍",
        "eagle": "🦅",
        "t_rex": "🦖",
        "shark": "🦈",
        "boar": "🐗",
        "camel": "🐫",
        "lion": "🦁",
        "cheetah": "🐆",
        "bear": "🐻",
        "fox": "🦊",
        "raccoon": "🦝",
        "dog": "🐶",
        "wolf": "🐺",
        "cat": "🐱",
        "tiger": "🐯",
        "lion_face": "🦁",
        "elephant": "🐘",
        "rhino": "🦏",
        "hippo": "🦛",
        "gorilla": "🦍",
        "monkey_1": "🐒",
        "monkey_2": "🐵",
        "horse_1": "🐎",
        "horse_2": "🐴",
        "unicorn": "🦄",
        "zebra": "🦓",
        "llama": "🦙",
        "kangaroo": "🦘",
        "crocodile": "🐊",
        "turtle": "🐢",
        "dolphin": "🐬",
        "whale": "🐳",
        "penguin": "🐧",
        "frog": "🐸",
        "owl": "🦉",
        "bat": "🦇",
        "rat": "🐀",
        "cow_2": "🐄",
        "cow_1": "🐮",
        "goat": "🐐",
        "ram": "🐏",
        "deer": "🦌",
        "ox": "🐂",
        "ant": "🐜",
        "spider": "🕷️",
        "bee": "🐝",
        "scorpion": "🦂",
        "crab": "🦀",
        "lobster": "🦞",
        "octopus": "🐙",
        "snail": "🐌",
        "koala": "🐨",

        "skull": "💀",
        "sleep": "😴",
        "skull_crossbones": "☠️",
        "fire": "🔥",
        "dice": "🎲",
        "heart": "❤️",
        "dynamite": "🧨",
        "evil_eye": "🧿",
        "web": "🕸️",
        "chains": "⛓️",

        "sports_medal": "🏅",
        "crown": "👑",
        "trident": "🔱",
        "rosette": "🏵️",
        "recruit_shield": "🔰",
        "snow_flake": "❄️",
        "thread": "🧵"
    }
    return emojis


class Dice:

    def __init__(self):
        self

    def roll(self, dice_num: int = 1):
        dice_values = [0] * 3
        for n in range(dice_num):
            dice_values[n] = random.randint(1, 6)
        dice = sorted(dice_values, reverse=True)
        return dice

    def attack_roll(self, attack_dice: int = 1):
        if not (0 < attack_dice < 4):
            raise ValueError("attack dice must between 1 and 4")
        dice = self.roll(attack_dice)
        return dice

    def defend_roll(self, defend_dice: int = 1):
        if not (0 < defend_dice < 4):
            raise ValueError("attack dice must between 1 and 4")
        dice = self.roll(defend_dice)
        return dice


class Player:

    def __init__(self, name, color, colors, symbol: str = None):
        self.name = name
        self.symbol = self.get_symbol(symbol)
        self.colors = colors
        self.color = color
        self.army = self.create_army()
        self.territories = []
        self.territory_count = 0
        self.continents = []
        self.cards = []
        self.hands_turned_in = 0
        self.income = self.calculate_income()
        self.total_army_size = 0
        self.play_order = 0
        self.battles = 0
        self.battles_lost = 0
        self.battles_won = 0
        self.win_ratio = float(0)
        self.battle_entry = {"role": [],  # attack or defend
                             "attacking_territory": [],
                             "defending_territory": [],
                             "defending_player": [],
                             "initial_strength": 0,
                             "own_casualties": 0,
                             "enemy_casualties": 0,
                             "average_dice_roll": 0,
                             "outcome": ""  # victory, retreat, defeat
                             }
        self.battles_log = []
        self.selected_cards = []
        self.unallocated_troops = 0

    def get_symbol(self, symbol: str = None):
        emojis = get_emojis()
        if not symbol:
            emoji_list = list(emojis.keys())
            return emojis[random.choice(emoji_list)]
        else:
            return emojis[symbol]

    def __str__(self):
        return self.name
        # return f"{self.colors["bg_color"]["black"]}{self.colors["text_color"][self.color]}<|{self.symbol} {self.name}|>{self.colors['text_color']['reset']}\n"

    def __repr__(self):
        return f"{self.colors["bg_color"]["dark_gray"]}{self.colors["text_color"][self.color]}{self.symbol} {self.colors["text_color"]["white"]}<| Name:{self.colors["text_color"][self.color]} {self.name}{self.colors["text_color"]["white"]}, Army Size:[{self.colors["text_color"][self.color]}{self.total_army_size}{self.colors["text_color"]["white"]}], Territories Occupied:[{self.colors["text_color"][self.color]}{self.count_territories()}{self.colors["text_color"]["white"]}], Income:[{self.colors["text_color"][self.color]}{self.income}{self.colors["text_color"]["white"]}]|>{self.colors['text_color']['reset']}\n"

    def attack(self, defending_territory: Territory, attacking_territory: Territory):

        if defending_territory not in attacking_territory.connections:
            raise ValueError("Territory not adjacent")
        if defending_territory in self.territories:
            raise ValueError("Territory already occupied")

        defending_troops = defending_territory.troops
        attacking_troops = attacking_territory.troops
        if defending_troops >= 2:
            defending_dice = 2
        else:
            defending_dice = defending_troops
        if attacking_troops >= 3:
            attacking_dice = 3
        else:
            attacking_dice = attacking_troops
        attacker_roll = Dice.attack_roll(attacking_dice)
        defender_roll = Dice.defend_roll(defending_dice)
        attacker_loss, defender_loss = compare_dice(attacker_roll, defender_roll)
        self.battle_entry["attacking_territory"].append(attacking_territory)

    def spawn(self, territory:Territory,troops:int):
        new_brigade = Brigade(territory, self, troops)
        self.army.brigades.append(new_brigade)
        territory.garrison = new_brigade
        return new_brigade


    def place_troop(self,game_data,territory_name: str,troops:int):
        territory = game_data.territories[territory_name]
        print(troops)
        print(self.unallocated_troops )
        print(territory.occupied_by)
        if self.unallocated_troops < troops:
            print("Not enough Troops")
        if territory.occupied_by == self:
            territory.garrison.reinforce(troops)
            self.unallocated_troops -= troops
            print(f"occupied: {self.unallocated_troops} - {troops}")

        if territory.occupied_by == 0:
            self.spawn(territory,troops)
            print(f"not occupied: {self.unallocated_troops} - {troops}")
            self.unallocated_troops -= troops
            print(f"Now occupied by: {territory.occupied_by}")


    def create_army(self):
        player_army = Army(self)
        return player_army

    def card_bonus(self):
        bonus_troops = self.hands_turned_in*2+4
        return bonus_troops

    def count_territories(self):
        self.territory_count = len(self.territories)
        return self.territory_count

    def calculate_income(self):
        income = math.floor(self.count_territories() / 3)
        if income < 3:
            income = 3
        self.income = income
        return income

    def turn_in_cards(self,game_data):
        selection = True
        choices = []
        while selection:
            choice = input("select cards to turn in : ")
            if choice == "d":
                selection = False
            elif choice in choices:
                print("Card already selected")
            choices.append(choice)

            if len(choices) >= 3:
                print("Done")
                selection = False

        selection = [int(i) - 1 for i in choices]
        selected_cards = [self.cards[i] for i in selection]
        self.selected_cards = selected_cards
        print(self.selected_cards)
        if self.validate():
            turn_in = input("Turn in hand? y/n ")
            if turn_in == "y":
                game_data.cards.discard_pile = [self.cards.pop(i) for i in selection]
                self.hands_turned_in += 1
                self.unallocated_troops = self.card_bonus()

                return selected_cards
        else:
            return print("Not a valid selection")

    def validate(self):
        hands = 0
        suits = {"artillery": {"instances": 0, "hands": 0},
                 "infantry": {"instances": 0, "hands": 0},
                 "calvary": {"instances": 0, "hands": 0},
                 "artillery": {"instances": 0, "hands": 0},
                 "wild": {"instances": 0, "hands": 0},
                 "combo": {"instances": 0, "hands": 0},
                 }

        for card in self.selected_cards:
            suits[card.suit]["instances"] += 1

        for suit in suits.keys():
            suits[suit]["hands"] = math.floor(suits[suit]["instances"] / 3)

        if suits["wild"]["instances"] == 1:
            for suit in suits.keys():
                if suits[suit]["instances"] == 2:
                    suits["wild"]["instances"] -= 1
                    suits[suit]["instances"] += 1


        if suits["infantry"]["instances"] == 1 and suits["calvary"]["instances"] == 1 and suits["artillery"][
            "instances"] == 1:
            suits["combo"]["hands"] = 1
        elif suits["infantry"]["instances"] == 1 and suits["calvary"]["instances"] == 1 and suits["wild"][
            "instances"] == 1:
            suits["combo"]["hands"] = 1
        elif suits["infantry"]["instances"] == 1 and suits["artillery"]["instances"] == 1 and suits["wild"][
            "instances"] == 1:
            suits["combo"]["hands"] = 1
        elif suits["calvary"]["instances"] == 1 and suits["artillery"]["instances"] == 1 and suits["wild"][
            "instances"] == 1:
            suits["combo"]["hands"] = 1
        elif suits["calvary"]["instances"] == 3:
            suits["calvary"]["hands"] = 1
        elif suits["artillery"]["instances"] == 3:
            suits["artillery"]["hands"] = 1
        elif suits["infantry"]["instances"] == 3:
            suits["infantry"]["hands"] = 1
        print(suits)
        for suit in suits.keys():
            hands += suits[suit]["hands"]
        if hands > 0:
            print("You have " + str(hands) + " hands")
            return True

        # hands = [total_artillery_hands, total_calvary_hands, total_infantry_hands, total_combination_hands]
        # labels = ["Total Artillery Hands", "Total Calvary Hands", "Total Infantry Hands", "Total Combination Hands"]
        # total_hands = sum(hands)
        # result = [(labels[n], i) for n, i in enumerate(hands) if i]
        # if total_hands >= 1:
        #     return True
        # else:
        #     return False


class Army:

    def __init__(self, player):
        self.brigades = []
        self.size = self.count_troops()
        self.player = player

    # def spawn_brigade(self):
    #
    #     new_brigade = Brigade(territory,self.player)
    #     self.brigades.append(new_brigade)
    # territory.garrison_troops(new_brigade)

    def count_troops(self):
        count = 0
        for brigade in self.brigades:
            count += brigade.size
        return count

    def merge_brigade(self, disbanding_brigade:Brigade, final_brigade):
        final_brigade.size += disbanding_brigade.size
        del disbanding_brigade
        return final_brigade

class Brigade:

    def __init__(self, territory: Territory, player: Player,size):
        self.size = size
        self.territory = territory
        self.colors = get_colors()
        territory.occupied_by = player
        player.territories.append(territory)
        self.player = player


    def casualties(self, troops_lost):
        self.size -= troops_lost
        return troops_lost

    def reinforce(self, troops_gained):
        self.size += troops_gained
        return troops_gained




    def __str__(self):
        return f"Strength: {self.size} {self.territory} {self.size} {self.player}"

    def __repr__(self):
        return f"<{self.player}'s {self.territory} Brigade: {self.size} Troop/s >"

        # return f"{self.colors["text_color"][self.player.color]}<{self.player}'s {self.territory} Brigade: {self.size} Troop/s >{self.colors["text_color"]["reset"]}"


class GameEngine:
    """World Map object that contains territory obejects"""

    def __init__(self):
        self.game_data = None
        self.territories = {}
        self.construct()
        self.colors = get_colors()
        self.continent_value = {"asia": 7,
                                "north_america": 5,
                                "europe": 5,
                                "africa": 3,
                                "south_america": 2,
                                "australia": 2}
        self.cards = RiskCardDeck(self)
        self.players = {}
        self.resolve_connections()

    def construct(self):
        self.game_data = pd.read_csv(r"database\game_data.csv")
        self.game_data[["continent_value", "x_cor", "y_cor", "troops"]] = self.game_data[
            ["continent_value", "x_cor", "y_cor", "troops"]].astype(int)
        self.game_data[["is_neutral"]] = self.game_data[["is_neutral"]].astype(bool)
        self.game_data[["occupied_by"]] = self.game_data[
            ["occupied_by"]].astype(bool)
        for n, i in enumerate(self.game_data.index):
            self.game_data.loc[n, "territory"] = self.game_data.loc[n, "territory"].replace(" ", "_")

        self.game_data = self.game_data.set_index("territory")

        for name in self.game_data.index.values:
            territory_obj = Territory(self.game_data.loc[name])
            attr_name = name.lower().replace(" ", "_")
            self.territories[name] = territory_obj
            setattr(self, attr_name, territory_obj)

    def resolve_connections(self):
        for territory_string in self.territories.keys():
            for n, _ in enumerate(getattr(self, territory_string).connections):
                neighbor_string = getattr(self, territory_string).connections[n]
                getattr(self, territory_string).connections[n] = getattr(self, neighbor_string)

    def create_player(self, player_name: str, player_color: str, symbol: str = None):
        player_object = Player(player_name, player_color, self.colors, symbol)
        self.players[player_name] = player_object
        return player_object

    def is_connected(self, territory1: Territory, territory2: Territory):
        if territory2 in territory1.connections:
            return True
        else:
            return False

    def is_connected_str(self, territory1: str, territory2: str):
        territory1 = self.territories[territory1]
        territory2 = self.territories[territory2]
        if territory2 in territory1.connections:
            return True
        else:
            return False



    def __iter__(self):
        for territory in self.game_data.index.values:
            yield getattr(self, territory)


class RiskCardDeck:

    def __init__(self, world_map: GameEngine):
        self.deck = self.build_deck(world_map)
        self.cards = self.shuffle_deck()
        self.discard_pile = []

    def build_deck(self, world_map):
        suit_symbols = {"infantry": "💂‍♂️", "calvary": "🏇", "artillery": "💣", "wild": "🧍🏇💣"}
        territory_list = [territory for territory in world_map.territories.keys()]
        cards = []
        wild_card = RiskCard(world_map.colors, "white", "Wild Card", "wild", suit_symbols["wild"], "None")
        cards.append(wild_card)
        cards.append(wild_card)
        for territory_name in territory_list:
            color = world_map.territories[territory_name].continent_color
            continent = world_map.territories[territory_name].continent_color
            suit = getattr(world_map, territory_name).card_suit
            suit_symbol = suit_symbols[f"{getattr(world_map, territory_name).card_suit}"]
            card_object = RiskCard(world_map.colors, color, territory_name, suit, suit_symbol, continent)
            cards += card_object
        return cards

    def shuffle_deck(self):
        shuffled_cards = []
        number_cards = len(self.deck)
        for n in range(0, number_cards):
            shuffled_cards.append(self.deck.pop(random.randint(0, len(self.deck) - 1)))
        shuffled_cards = self.split_deck(shuffled_cards)
        return shuffled_cards

    def split_deck(self, cards):
        middle = int(len(cards) / 2)
        variation = int(len(cards) * .1 / 2)
        middle_low = middle - variation
        middle_high = middle + variation
        middle = random.randint(middle_low, middle_high)
        split_deck_1 = cards[:middle]
        split_deck_2 = cards[middle:]
        cards = split_deck_2 + split_deck_1
        return cards

    def deal_card(self, number_human_players: int = 1, npp: int = 1):
        return self.cards.pop()

    def deal_cards(self, number_cards: int, player: Player):
        for _ in range(number_cards):
            player.cards.append(self.deal_card())

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        deck_string = ""
        for card in self.cards:
            deck_string += str(card)
        deck_string = deck_string + "\n"
        return deck_string

    def __repr__(self):
        deck_size = len(self.cards)
        deck_string = ""
        for card in self.cards:
            deck_string += str(card)
        deck_string = f" {deck_size} Cards\n{deck_string} + \n"
        return deck_string

    def __iter__(self):
        for card in self.cards:
            yield card


class CardsHand:

    def __init__(self, player: Player):
        self.player = player
        self.cards = player.cards
        self.combinations()


class RiskCard:

    def __init__(self, colors, color, name, suits, symbol, continent):
        self.name = name
        self.suit = suits
        self.symbol = symbol
        self.color = color
        self.continent = continent
        self.colors = colors

    def __iter__(self):
        yield self

    def __str__(self):
        """
        Creates a viusal display of the cards
        :param cards:
        :return: None
        """
        BOLD = "\033[1m"

        return f"{self.colors["bg_color"]["black"]}{self.colors["text_color"][self.color]}|{self.name.title().replace("_", " ")} {self.symbol}|{self.colors["text_color"]["reset"]}"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    pass
## Test GameEngine Class
game_engine = GameEngine()

# test cards method
# test __repr__
# print(f"{game_engine.cards=}")

# test __str__
# print(f"{game_engine.cards}")


# Test creating players -> no need to assign players to variable.
game_engine.create_player("John", "red", "rhino")
game_engine.create_player("Morgan", "magenta", "unicorn")
game_engine.players["John"].unallocated_troops = 50
# print(game_engine.territories)
# print(game_engine.players)
# game_engine.players["John"].place_troop(game_engine,"alaska",4)

for n, territory in enumerate(game_engine.territories.keys()):
    if n < 20:
        game_engine.players["John"].place_troop(game_engine,territory,2)
    else:
        pass

print(f"{game_engine.alaska=}")

print(f"John occupies {game_engine.players["John"].territories}")
print(f"John income {game_engine.players["John"].income}")
print(f"John Brigades: {game_engine.players["John"].army.brigades}")
print(f"Total Troops: {game_engine.players["John"].army.count_troops()}")
print(f"{game_engine.players['John'].cards}")
game_engine.cards.deal_cards(15, game_engine.players["John"])
print(f"{game_engine.players['John'].cards}")
game_engine.players['John'].turn_in_cards(game_engine)
print(game_engine.cards.discard_pile)
