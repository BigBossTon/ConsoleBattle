import random
import copy

from battle.Battle import Battle
from character.warrior import Warrior
from character.archer import Archer
from character.mage import Mage

names = ('Dave', 'Rick', 'Shelly', 'Mona', 'Lobster')

characters = {
    'warrior': Warrior('name', 10, 100, (0, 2)),
    'archer': Archer('name', 15, 75, (-2, 3)),
    'mage': Mage('name', 20, 60, (-5, 5))
}


def random_choice_of_character(character):
    choice = random.choice(tuple(character.keys()))
    player = copy.copy(character[choice])
    player.name = random.choice(names)
    return player


def yes_no(string):
    return string.lower().strip() == 'y'

def restart():
    while True:
        choice = input('Желаете сыграть снова? y/n')
        if yes_no(choice):
            return True
        return False


def choice_of_character(character):
    name = input('Придумайте имя персонажу:')
    while True:
        choice = input('1. Warrior\n2. Archer\n3. Mage\nВыбери своего героя:')
        if choice.strip() == '1':
            print(Warrior(name, 10, 100, (0, 2)))
            if yes_no(input('Вы уверены с выбором персонажа? y/n:')):
                player = copy.copy(character['warrior'])
                player.name = name
                return player
        elif choice.strip() == '2':
            print(Archer(name, 15, 75, (-2, 3)))
            if yes_no(input('Вы уверены с выбором персонажа? y/n:')):
                player = copy.copy(character['archer'])
                player.name = name
                return player
        elif choice.strip() == '3':
            print(Mage(name, 20, 60, (-5, 5)))
            if yes_no(input('Вы уверены с выбором персонажа? y/n:')):
                player = copy.copy(character['mage'])
                player.name = name
                return player


def main():
    while True:
        computer_enemy = random_choice_of_character(characters)
        player_enemy = choice_of_character(characters)
        battle = Battle(player_enemy, computer_enemy)

        while not battle.end_of_battle():
            battle.fight()
        print(battle.winner())

        if not restart():
            break
    battle.save_log('logs.json')

if __name__ == '__main__':
    main()
