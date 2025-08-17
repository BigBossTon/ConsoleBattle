from random import *
from .base import Base


class Mage(Base):
    def doDamage(self, person: Base):
        damage = randint(self.damageHP + self.damageRange[0], self.damageHP + self.damageRange[1])
        person.takeDamage(damage)
        return f'{self.name} прочел заклинание и нанес {damage} урона.'




