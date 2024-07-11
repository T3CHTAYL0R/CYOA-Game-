import sys

class Adventurer:
    def __init__(self, name, character_class):
        self.name = name
        self.charcter_class = character_class
        self.health = self.set_base_health()
        self.attack = self.set_base_attack()
        self.defense = self.set_base_defense()
        self.inventory = []

    def __str__(self):
        return f"{self.name} the {self.character_class}"

    def set_base_health(self):
        if self.character_class == "Barbarian":
            return 200

def main():
    #Get the player name
    player_name = input("Type your name: ")
    print("Welcome,", name)

    while True:
        response = input("Are you ready for your adventure? (yes/no): ").strip().lower()
        if response == "yes":
            print("Let's Begin")
            start_adventure(player_name)
            break
        elif response == "no":
            print("Maybe next time!")
            sys.exit()

        else:
            print("Please enter 'yes' or 'no'.")

def start_adventure(player_name):
    print("You are Dead")
