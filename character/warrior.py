from random import *

from .base import Base


class Warrior(Base):
    def doDamage(self, person):
        damage = randint(self.damageHP - self.damageRange[0], self.damageHP + self.damageRange[1])
        person.takeDamage(damage)
        return f'{self.name} взмахнул мечом и нанес {damage} урона.'

    def blockAttack(self, attack):
        pass
