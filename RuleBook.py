import pandas as pd
from typing import Literal


class GameData:
    text_format = {
        "bold": "\033[1m",
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

    colors = {"text_color": text_format, "bg_color": bg_colors}

    suit_symbols = {"infantry": "💂‍♂️", "calvary": "🏇", "artillery": "💣", "wild": "🧍🏇💣"}
    # 🔫💥🎯
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
        "peasant": "👨‍🌾",
        "super_villain": "🦹‍♂️",
        "merman": "🧜‍♂️",
        "infantry": "💂‍",
        "astronaut": "👨‍🚀",
        "battle": "⚔️",
        "sword":"🗡️",
        "defend": "🛡️",
        "garrison":"🏰",
        "white_flag": "🏳️",
        "Dice":"🎲",
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

    def __init__(self):
        self.data = None
        self.csv = None
        self.territories: dict[str:str] = {}
        self.connections: dict[str:list[str]] = {}
        self.continents_names: list[str] = []
        self.continents: dict[str:dict[str:str]] = {}
        self.get_game_data()
        self.init_connections()

    def _fetch_csv(self):
        self.csv = pd.read_csv(r"database\game_data.csv")
        return self.csv

    def _set_data_types(self):
        self.csv[["continent_value", "x_cor", "y_cor"]] = self.csv[
            ["continent_value", "x_cor", "y_cor"]].astype(int)
        for n, i in enumerate(self.csv.index):
            self.csv.loc[n, "territory"] = self.csv.loc[n, "territory"].replace(" ", "_")
        self.data = self.csv.set_index("territory")

    def _create_map_properties_dictionaries(self):
        for n, territory in enumerate(self.data.index):
            continent = self.data.loc[territory, "continent"]
            card_suit = self.data.loc[territory, "card_suit"]
            self.territories[territory] = {"continent": continent,
                                           "card_suit": card_suit}
            self.continents_names.append(continent)
        self.continents_names = list(dict.fromkeys(self.continents).keys())

    def _populate_dictionary(self):
        for n, territory in enumerate(self.data.index):
            color = self.data.loc[territory, "continent_color"]
            continent = self.data.loc[territory, "continent"]
            value = int(self.data.loc[territory, "continent_value"])
            if continent not in self.continents.keys():
                self.continents[continent] = {"color": color,
                                              "value": value,
                                              "territories": [territory]}
            else:
                self.continents[continent]["territories"].append(territory)

    def get_game_data(self):
        self._fetch_csv()
        self._set_data_types()
        self._create_map_properties_dictionaries()
        self._populate_dictionary()

    def get_player_rules(self, number_of_players: int,
                         rule: Literal["neutral_players", "initial_troops", "initial_cards"] = None):
        self.rules = pd.read_csv(r"database\rules.csv")
        self.rules = self.rules.set_index("number_players")
        self.rules[["neutral_players", "initial_troops", "initial_cards"]] = self.rules[
            ["neutral_players", "initial_troops", "initial_cards"]].astype(int)
        info_row = self.rules.loc[number_of_players]
        return info_row

    def init_connections(self):
        for n, territory in enumerate(self.data.index):
            connection_list = self.data.loc[territory, "connections"].split(",")
            for n, connected in enumerate(connection_list):
                connection_list[n] = connected.strip().replace(" ", "_")
                self.connections[territory] = connection_list
        return self.connections



game_data = GameData()
if __name__ == "__main__":
    print(game_data.get_player_rules(2))
#
# print(game_data.continents["north_america"]["color"])
# print(game_data.continents["north_america"])
#     # for territory in game_data.territory_names:
#     #     territory
# print(game_data.emojis["wizard"])
