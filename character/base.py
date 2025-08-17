from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, name='Dave', damage_hp=0, heal_point=0, damage_range=(0,0)):
        self.name = name
        self.damageHP = damage_hp
        self.healPoint = heal_point
        self.damageRange = damage_range

    @abstractmethod
    def doDamage(self, person):
        pass

    def isAlive(self):
        return self.healPoint > 0

    def takeDamage(self, damage):
        self.healPoint = max(0, self.healPoint - damage)

    def __str__(self):
        return (f'Имя: {self.name},\nКласс: {self.__class__.__name__},\nУрон: '
                f'{self.damageHP + self.damageRange[0]}-{self.damageHP + self.damageRange[1]}\n'
                f'Очки здоровья:{self.healPoint}')