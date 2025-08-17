from random import *

from .base import Base


class Archer(Base):
    def doDamage(self, person: Base):
        damage = randint(self.damageHP + self.damageRange[0], self.damageHP + self.damageRange[1])
        person.takeDamage(damage)
        return f'{self.name} выстрелил из лука и нанес {damage} урона.'

    def dodge(self):
        pass
