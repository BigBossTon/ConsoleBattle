import pytest
from character.warrior import Warrior
from character.archer import Archer
from character.mage import Mage


@pytest.fixture
def warrior():
    return Warrior('Name', 10, 100, (0, 2))


@pytest.fixture
def archer():
    return Archer('Name', 15, 75, (-2, 3))


@pytest.fixture
def mage():
    return Mage('Name', 20, 60, (-5, 5))


def test_is_alive(warrior):
    assert warrior.isAlive()


def test_take_damage(warrior):
    prev_hp = warrior.healPoint
    warrior.takeDamage(20)
    assert warrior.healPoint == max(prev_hp - 20, 0)


def test_doDamage(warrior, archer, mage):
    warrior_hp_old = warrior.healPoint
    archer_hp_old = archer.healPoint
    warrior.doDamage(archer)
    assert archer.healPoint in range(archer_hp_old - (warrior.damageHP + warrior.damageRange[1]),
                                     archer_hp_old - (warrior.damageHP + warrior.damageRange[0]) + 1)
    archer.doDamage(warrior)
    assert warrior.healPoint in range(warrior_hp_old - (archer.damageHP + archer.damageRange[1]),
                                      warrior_hp_old - (archer.damageHP + archer.damageRange[0]) + 1)
    warrior_hp_old = warrior.healPoint
    mage.doDamage(warrior)
    assert warrior.healPoint in range(warrior_hp_old - (mage.damageHP + mage.damageRange[1]),
                                      warrior_hp_old - (mage.damageHP + mage.damageRange[0]) + 1)
