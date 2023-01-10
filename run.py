# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# General Unit

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"Unit {name} is created.")

    def move(self, location):
        print("{0} is moving toward {1} : Speed [{2}]".format(self.name, location, self.speed))
       
    def damaged(self, damage):
        print("{0} : {1} damaged.".format(self.name, damage))
        self.hp -= damage
        print("{0} : Current Lvl of attacking is {1}.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} is destroyed.".format(self.name))
"""
Using method overriding
"""
# Attack Unit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("Unit {0} is attacking from {1}. [Lvl. of attacking is {2}]".format(self.name, location, self.damage))
