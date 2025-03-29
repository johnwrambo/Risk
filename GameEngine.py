from RuleBook import GameData, game_data
from Dice import BattleDice, battle_dice
from RiskCards import deck, PlayerDeck
from NameGenerator import brigade_name


class Territory:
    """Class that defines a territory, owned by Map."""

    def __init__(self, territory_name: any, continent: str, color: str):
        self.name = territory_name
        self.title = self.name.title().replace("_", " ")
        self.continent = continent
        self.continent_title = self.continent.title().replace("_", " ")
        self.color = color
        self.garrison = None
        self.who()

    def __str__(self):
        print_string = str(self.title)
        return f"{print_string} Territory"

    def __repr__(self):
        return f"<Territory Object:{self.name}>"

    def garrison_troops(self, brigade):
        self.garrison = brigade

    def info(self):
        if not self.owner:
            garrison = "and is unoccupied."
        else:
            garrison = f"and is controlled by Commander {self.owner} and holds a garrison of {self.garrison.size} troops."

        info_string = f"{self.title} is in {self.continent_title} {garrison}"
        return info_string

    def who(self):
        if self.garrison:
            setattr(self, "occupied_by", self.garrison.commander)
            return self
            # f"Occupied by {self.garrison.commander}'s {self.garrison.name}"

        else:
            setattr(self, "occupied_by", None)
            return self


class Map:
    """Class that defines a map, owned by GameEngine."""

    def __init__(self):
        self.continents = {}
        self.territories = {}  # String finds territory object
        self.connections = {}  # String finds connected objects


class Brigade:
    """Brigade holds troop numbers for a given territory, owned by Army and territory"""

    def __init__(self, size, brigade_name, commander:Player, territory: Territory = None):
        self.brigade_name = brigade_name # Mascot
        self.commander = commander
        self.size = size
        self.moves = 1
        self.territory = territory
        self.company = 1
        self.total_casualties = 0
        self.status_icon = game_data.emojis["infantry"]
        self.status = "Alive"

    def die(self):
        self.moves = 0
        self.territory = None
        self.status = "Dead"
        self.status_icon = game_data.emojis["skull"]

    def split(self, detachment: int):
        max_det = self.size - 1
        if self.size - detachment > 0:
            self.take_casualties(detachment)
            if self.company == 1:
                suf = "st"
            elif self.company == 2:
                suf = "nd"
            elif self.company == 3:
                suf = "rd"
            else:
                suf = "th"
            name = f"{self.brigade_name} Brigade, 50{self.company}{suf} Co."
            attack_brigade = Brigade(detachment, name, self.commander, self.territory)
            self.company += 1
            return attack_brigade
        else:
            raise ValueError(f"Cannot detach that many troops, maximum detachment size is {max_det}")

    def take_casualties(self, troops_lost):
        self.size -= troops_lost
        self.total_casualties += troops_lost
        return self

    def reinforce(self, troops_gained):
        self.size += troops_gained
        return self

    def locate(self, map):
        map.territories.keys()

    def __str__(self):
        return f"{self.brigade_name}"

    def __repr__(self):
        return f"<{self.status_icon}{self.territory} corps, {self.brigade_name} Brigade: {self.size} Troop/s >"

        # return f"{game_data.colors["text_color"][self.player.color]}<{self.player}'s {self.territory} Brigade: {self.size} Troop/s >{game_data.colors["text_color"]["reset"]}"


class Army:

    def __init__(self, player):
        self.brigades = []
        self.brigades_lost = []
        self.general = player

    def total_troops(self):
        count = 0
        for brigade in self.brigades:
            count += brigade.size
        return count

    def merge_brigade(self, disbanding_brigade: Brigade, final_brigade):
        final_brigade.size += disbanding_brigade.size
        del disbanding_brigade
        return final_brigade


class Player:

    def __init__(self, engine, name, color, symbol: str = None):
        self.engine = engine
        self.name = name
        self.player_number = None
        self.symbol = game_data.emojis[symbol]
        self.color = color
        self.army = None
        self.unallocated_troops = 0
        self.territories = []
        self.cards = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<{self.name}>"

    def attack(self, attacking_territory: Territory, defending_territory: Territory, troops: int):
        attack = True
        while attack:
            attacking_brigade = attacking_territory.garrison.split(troops)
            attacking_brigade.status_icon = game_data.emojis["battle"]
            self.army.brigades.append(attacking_brigade)
            attacking_troop_size = attacking_brigade.size
            defending_brigade = defending_territory.garrison
            defending_troop_size = defending_brigade.size
            defending_brigade.status_icon = game_data.emojis["defend"]
            if attacking_troop_size <= 0:
                raise ValueError("No more troops sir!")
            else:
                attacker_losses, defender_losses = battle_dice.battle(attacking_troop_size, defending_troop_size)
                attacking_brigade.take_casualties(attacker_losses)
                defending_brigade.take_casualties(defender_losses)
                if defending_brigade.size <= 0:
                    print("DEFENDING TROOPS DEFEATED")
                    attacking_brigade.territory = defending_territory
                    defending_territory.garrison = attacking_brigade
                    self.engine.kill(defending_brigade)
                if attacking_brigade.size <= 0:
                    print("Attacking TROOPS DEFEATED")
                    self.engine.kill(attacking_brigade)

            result_string = f"{attacking_territory.name} attacked {defending_territory.name}, attackers sustained {attacker_losses} casualties, defenders sustained {defender_losses} Attacker has {attacking_brigade.size} troops left, defender has {defending_brigade.size} troops."
        attack_again = input(f"{result_string} attack againt?")
        if attack_again == "n":
            attack = False
        elif attack_again == "r":
            self.army.merge(attacking_brigade, attacking_territory.garrison)
            attack = False
            print(f"{attacking_brigade} retreated with {attacking_brigade.size} troops")
        return [attacking_brigade.size, defending_brigade.size, attacker_losses, defender_losses, result_string]

    def inventory(self):
        occupied_territories = [brigade.territory for brigade in self.army.brigades]
        self.territories = occupied_territories
        troops = self.unallocated_troops
        return f"{self.name}'s Inventory: {troops} Troops, {len(self.cards)} Cards, {len(self.territories)} Territories"

    # def get_territories(self):
    #     for brigade in self.army.brigades:
    #         controlled_territories = brigade.territory
    #         self.territories.append(controlled_territories)
    #     return self.territories
    def attack_options(self):
        target_options = []
        for territory in self.territories:
            for target_territory in territory.connections:
                # print(f"{target_territory=}")
                # print(f"who? {target_territory.occupied_by=}")
                if target_territory.occupied_by != self:
                    # print(f"From: {territory}->{target_territory} occupied by {target_territory.occupied_by} is a valid target")
                    target_options.append((territory.name, target_territory))
                # else:
                # print(f"From: {territory}->{target_territory} occupied by {target_territory.occupied_by} is NOT a valid target")

        self.target_options = target_options
        return self.target_options

    # def kill(self,brigade_name: str):
    #     self.
    #      brigade_object = getattr(self.gamap, brigade_name)


class GameEngine:
    """World Map object that contains territory objects"""

    def __init__(self):
        self.players = {}
        self.all_brigades = {}
        self.dead_brigades = {}
        self.board = {}
        self.brigade_names = []
        self.map = Map()
        self._build_map()
        self._resolve_connections()
        self.number_of_players = 0
        deck.shuffle_deck()

    def _build_map(self):
        for territory_name in game_data.territories.keys():
            continent = game_data.territories[territory_name]["continent"]
            self.map.connections = game_data.connections
            color = game_data.continents[continent]["color"]
            # 🌍 Create Territory Object --
            territory_object = Territory(territory_name, continent, color)
            self.map.territories[territory_name] = territory_object
            setattr(self.map, territory_name, territory_object)
            self.map.continents = game_data.continents

    def name_brigade(self):
        """Generates a random name for a brigade, and check if the brigade name already exists"""
        name = brigade_name()
        while name in self.brigade_names:
            name = brigade_name()
        self.brigade_names.append(name)
        return name

    def _resolve_territory(self, territory: str) -> Territory:
        """ get territory object from territory string
        :return:
        """
        territory_object = getattr(self.map, territory)
        return territory_object

    def _resolve_connections(self):
        """ Changes list of connected territories from a list of strings
        to a list of objects
        :return:
        """
        for territory in game_data.connections.keys():
            neighbors = game_data.connections[territory]
            # print(f"{territory} has neighrbors: {neighbors=}")
            for n, neighbor in enumerate(neighbors):
                # print(f"{getattr(self.map, territory)} has neighrbor: {neighbor=}")
                self.map.connections[territory][n] = getattr(self.map, neighbor)

            setattr(self.map.territories[territory], "connections", self.map.connections[territory])

    def _resolve_territories(self):
        for player_string in self.players.keys():
            player_object = self.players[player_string]
            for n, territory_string in enumerate(player_object.territories):
                player_object.territories[n] = getattr(self.map, territory_string)
                player_object.territories[n].who()

    def create_player(self, engine, player_name: str, player_color: str, symbol: str = None):
        player_object = Player(engine, player_name, player_color, symbol)
        self.players[player_name] = player_object
        setattr(self, player_name, player_object)
        self.number_of_players += 1
        player_object.player_number = self.number_of_players
        return player_object

    def kill(self, brigade_object: Brigade):
        brigade_object.die()
        dead_index = brigade_object.commander.army.brigades.index(brigade_object)
        self.dead_brigades[brigade_object.brigade_name] = brigade_object.commander.army.brigades.pop(dead_index)
        return self

    def initialize_players(self, cards: int = 13):

        number_of_players = len(self.players)
        troops = game_data.get_player_rules(number_of_players)["initial_troops"]
        card_number = game_data.get_player_rules(number_of_players)["initial_cards"]
        neutral_players = game_data.get_player_rules(number_of_players)["neutral_players"]
        if int(neutral_players) > 0:
            self.create_player(self, "neutral_players", "purple", "peasant")
        for player_name in self.players.keys():
            # Get player object
            player_object = self.players[player_name]
            # print(f"{player_object.cards=}")
            # initialize with 40 troops
            setattr(player_object, "unallocated_troops", troops)
            # initialize Army object and assign to player object
            setattr(player_object, "army", Army(player_object))
            # Deal cards to player based on number of players
            if number_of_players == 2:
                player_object.cards.extend(deck.deal_cards(card_number))
            for card_object in player_object.cards:
                # print(f">M{player_object.cards=}")
                # print(f"{card_object} {player_object}")
                territory = card_object.territory
                player_object.territories.append(card_object.territory)
                mascot = self.name_brigade()
                new_brigade = Brigade(1, mascot, player_object, self._resolve_territory(territory))
                player_object.army.brigades.append(new_brigade)
                # print(f">Brigades: {player_object.army.brigades=}")
                self.map.territories[territory].garrison = new_brigade
                self.map.territories[territory].garrison.occupied_by = player_object
            # for brigade in player_object.army.brigades:
            #     # print(f"{brigade.territory=}")

            deck.discard(player_object.cards)
            # player_object.get_territories()
        self._resolve_territories()
        self.set_board()
        return player_object

    def place_troops(self, territory: str, troops: int):
        self.map.territories[territory].garrison.reinforce(troops)
        return self.map.territories[territory].garrison

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

    def set_board(self):
        for territory in self.map.territories.keys():
            # print(f"{self.map.territories[territory].who().occupied_by}")
            if self.map.territories[territory].garrison:
                occupier = self.map.territories[territory].garrison.commander
                # territory = self._resolve_territory(territory)
                self.board[territory] = occupier
            else:
                pass
            # print(f"{territory} occupied by {self.map.territories[territory].who().occupied_by}")

    def __iter__(self):
        for territory in self.game_data.index.values:
            yield getattr(self, territory)


class TurnManager(GameEngine):

    def __init__(self):
        super().__init__()
        self.turn_count = 0


if __name__ == "__main__":
    ## Test GameEngine Class

    game_engine = GameEngine()
    # print(f"{game_engine.map.connections["alaska"]}")

    game_engine.create_player(game_engine, "John", "red", "wizard")
    game_engine.create_player(game_engine, "Jack", "blue", "spider")

    game_engine.initialize_players()
    # print(f"{game_engine.John.territories=}")
    # print(f"{game_engine.Jack.territories=}")
    # print(f"{game_engine.John.inventory()}")
    # # print(f"{game_engine.Jack.inventory()}")
    # print(f"{game_engine.John.army.brigades}")
    print(f"{game_engine.John.attack_options()=}")

    # print(game_engine.map.territories[game_engine.John.territories[0]].garrison)
game = True
# while game:
#     print(game_engine.board)
#     command = input("what do you want to do?")
#     exec(command)
