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

# Marine
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5) # name, hp, speed, Lvl of attacking

    # Stimpack : increasing moving speed but hp level decreases -10
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{name} is using stimpack. HP decrease by 10")
        else:
            print(f"{name} is not able to use stimpack with lack of HP")

# Tank
class Tank(AttackUnit):
    # Siege mode : No ability to move, it sticks on the ground and attacking more powerfully
    siege_developed = False # wether siege mode is developing (a class variable)

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35) # name, hp, speed, Lvl of attacking
        self.siege_mode = False # (Easy) the siege mode

    # Siege Mode
    def set_siege_mode(self):
        if Tank.siege_developed == False # leaving the method when siege_mode is not developing
            return

        # currently it's not siege_mode
        if self.siege_mode == False:
            print(f"{name} : Switching to Siege Mode")
            self.damage *= 2 # hp increases twice
            self.siege_mode = True # Set siege mode
        # currently it's siege_mode
        else:
            print(f"{name} : Clearing the Siege Mode")
            self.damage /= 2 # hp decreases to half
            self.siege_mode = False # Clear siege mode
