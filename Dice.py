import random
from RuleBook import GameData as gd

class BattleDice:
    """Class that defines the dice and roll mechanics owned by GameEngine"""

    def __init__(self):
        self.init_roll = 0
        self.roll_values = 0
        self.attack_roll_values =0
        self.defense_roll_values =0
        self.attack_result = None
        self.defend_result = None

    def roll(self, dice_num: int = 1) -> list[int]:
        dice_values = [0] * 3
        for n in range(dice_num):
            dice_values[n] = random.randint(1, 6)
        self.roll_values = sorted(dice_values, reverse=True)

        return self.roll_values

    def attack_roll(self, attacking_troops: int = 1):
        if attacking_troops > 3:
            attack_dice = 3
        else:
            attack_dice = attacking_troops
        self.attack_roll_values = self.roll(attack_dice)
        attack_roll = ''.join([str([die]) for die in self.attack_roll_values if die !=0])
        self.attack_result = f"{gd.colors["text_color"]['bold']}{gd.colors["text_color"]['white']}{gd.bg_colors["red"]}{attack_roll}{gd.colors["text_color"]['reset']}"
        return self.attack_roll_values

    def defend_roll(self, defending_troops: int = 1):
        if defending_troops > 3:
            defend_dice = 3
        else:
            defend_dice = defending_troops
        self.defend_roll_values = self.roll(defend_dice)
        defend_roll = ''.join([str([die]) for die in self.defend_roll_values if die !=0])
        self.defend_result = f"{gd.colors["text_color"]['bold']}{gd.colors["text_color"]['white']}{gd.bg_colors["blue"]}{defend_roll}{gd.colors["text_color"]['reset']}"

        return self.defend_roll_values

    def compare_rolls(self, attacker: list[int], defender: list[int]) -> tuple:
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
        return sum(attacker_losses), sum(defender_losses)

    def battle(self, attacker_dice_number: int, defender_dice_number: int) -> tuple:
        attacker = self.attack_roll(attacker_dice_number)
        defender = self.defend_roll(defender_dice_number)
        attacker_losses, defender_losses = self.compare_rolls(attacker, defender)
        return attacker_losses, defender_losses

    def __str__(self):
        return f"{self.roll_values}"

    def display_results(self):
        attack_roll = ''.join([str([die]) for die in self.attack_roll_values if die !=0])
        defend_roll = ''.join([str([die]) for die in self.defend_roll_values if die !=0])
        attack_string = f"{gd.emojis["dice"]}{gd.colors["text_color"]['bold']}{gd.colors["text_color"]['white']}{gd.bg_colors["red"]}{attack_roll}{gd.colors["text_color"]['reset']}"
        defend_string = f"{gd.emojis["dice"]}{gd.colors["text_color"]['bold']}{gd.colors["text_color"]['white']}{gd.bg_colors["blue"]}{defend_roll}{gd.colors["text_color"]['reset']}"
        return print(f"{attack_string}\n{defend_string}")

battle_dice = BattleDice()

if __name__ == "__main__":

    print(battle_dice.attack_roll(3))
    print(battle_dice.defend_roll(2))
    # battle_dice.battle(3,2)
    battle_dice.display_results()