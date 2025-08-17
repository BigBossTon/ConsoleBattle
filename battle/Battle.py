from mixins.logger import logger

class Battle(logger):

    def __init__(self, player, enemy):
        self.player_turn = True
        self.player = player
        self.enemy = enemy
        pass

    def fight(self):
        if self.player_turn:
            message = self.player.doDamage(self.enemy)
        else:
            message = self.enemy.doDamage(self.player)
        print(message)
        print(f'Здоровье {self.player.name}: {self.player.healPoint}, здоровье {self.enemy.name}: {self.enemy.healPoint}')
        self.log(message)
        self.player_turn = not self.player_turn

    def end_of_battle(self):
        return not (self.player.healPoint and self.enemy.healPoint)

    def winner(self):
        if self.player.healPoint:
            return f'В этой схватке победу одержал {self.player.name}'
        return f'В этой схватке победу одержал {self.enemy.name}'

