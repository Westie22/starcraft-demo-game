# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# General Unit

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} unit is created.")
        print(f"Strength {hp}, Lvl. of attacking is {damage}")
"""
Using method overriding
"""
# Attack Unit
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : from {1} attacking. [Lvl. of attacking is {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} damaged.".format(self.name, damage))
        self.hp -= damage
        print("{0} : Current Lvl of attacking is {1}.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} is destroyed.".format(self.name))

# Firebat : Attacking unit, ability of fire-gun
firebat1 = AttackUnit("Firebat", 50, 16)
firebat1.attack("From 5 o'clock")

# Attacked twice
firebat1.damaged(25)
firebat1.damaged(25)