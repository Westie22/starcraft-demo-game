from random import *
player_input = input("Press Enter to play the game!!: \n")

# General Unit


class Unit:
    """
    Basic Unit class that whenever an unit created,
    print out of which unit has been created.
    With move(), it print out of Unit's movement status.
    Damage() excluding AttackUnit.
    """
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"Unit {name} is created.")

    def move(self, location):
        print("{0} is moving toward {1} : Speed [{2}]"
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} damaged.".format(self.name, damage))
        self.hp -= damage
        print("{0} : Current Lvl of attacking is {1}."
              .format(self.name, self.hp))
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
        print("Unit {0} is attacking from {1}. [Lvl. of attacking is {2}]"
              .format(self.name, location, self.damage))

# Marine


class Marine(AttackUnit):
    def __init__(self):
        # name, hp, speed, Lvl of attacking
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    # Stimpack : increasing moving speed but hp level decreases -10
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} is using stimpack. HP decrease by 10".format(self.name))
        else:
            print("{0} is not able to use stimpack with lack of HP"
                  .format(self.name))

# Tank


class Tank(AttackUnit):
    """
    Siege mode
    No ability to move, it sticks on the ground and attacking more powerfully
    wether siege mode is developing (a class variable)
    """
    siege_developed = False

    def __init__(self):
        # name, hp, speed, Lvl of attacking
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        # (Easy) the siege mode
        self.siege_mode = False

    # Siege Mode
    def set_siege_mode(self):
        # leaving the method when siege_mode is not developing
        if Tank.siege_developed:
            return

        # currently it's not siege_mode
        if self.siege_mode:
            print("{0} : Switching to Siege Mode".format(self.name))
            # hp increases twice
            self.damage *= 2
            # Set siege mode
            self.siege_mode = True
        # currently it's siege_mode
        else:
            print("{0} : Clearing the Siege Mode".format(self.name))
            # hp decreases to half
            self.damage /= 2
            # Clear siege mode
            self.siege_mode = False

# Flyable function class


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} is flying toward {1} : Speed [{2}]"
              .format(name, location, self.flying_speed))

# Flyable Attack Unit


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        # with flying speed, there is no speed on the ground, it sets as 0
        Flyable.__init__(self, flying_speed)
    # Initializong move from Unit class - overriding

    def move(self, location):
        self.fly(self.name, location)
# Another flyable attack unit Wraith that has a special skill called 'cloaking'


class Wraith(FlyableAttackUnit):
    def __init__(self):
        # hp, Lvl of attacking, flying speed
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        # cloaking mode(cleared)
        self.cloaked = False

    def cloaking(self):
        # when it's a cloaking mode
        if self.cloaked:
            print("Clearing Cloaking Mode for {0}.".format(self.name))
            self.cloaked = False
            # when it's NOT a cloaking mode
        else:
            print("Setting Cloaking Mode for {0}.".format(self.name))
            self.cloaked = True

# Game start


def game_start():
    print("=" * 31)
    print("Welcome to StarCraft Demo Game!")
    print("Let's strat the game!!")
    print("=" * 31)

# Game over


def game_over():
    print("=" * 52)
    print("[Player] : Too much damaged, but it was a good game!")
    print("[Player] : Left the game")
    print("=" * 52)

# Actual game starts


game_start()

create_unite_input = input("Press Enter to create your Units: \n")
# Create 3 Marines
m1 = Marine()
m2 = Marine()
m3 = Marine()
print("-" * 23)

# Create 2 Tanks
create_tank_input = input("Press Enter to create Tank: \n")
t1 = Tank()
t2 = Tank()
print("-" * 22)

# Create 1 Wraith
create_wraith_input = input("Press Enter to create Wraith: \n")
w1 = Wraith()
print("-" * 23)

# General units management (all created ones avbove, append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# All units are moving
moving_input = input("Press Enter to move your weapons: \n")
for unit in attack_units:
    unit.move("1 O'Clock")
print("-" * 45)

# Developing Tank Siege mode
mode_input = input("Press Enter to set special mode & attacking: \n")
Tank.siege_developed = True
print("Developing Tank Siege mode is complete.")

# Ready for all to be attacking mode
for unit in attack_units:
    if isinstance(unit, Marine):  # Marine's instance then stimpack
        unit.stimpack()
    elif isinstance(unit, Tank):  # Tank's instance then siege mode
        unit.set_siege_mode()
    elif isinstance(unit, Wraith):  # Wraith' instance then cloaking
        unit.cloaking()

# All units attack
for unit in attack_units:
    unit.attack("1 O'Clock")

# All units damaged
for unit in attack_units:
    # receiving attacks randomly ( 5 ~ 20)
    unit.damaged(randint(5, 20))

# Quit the game
x = input("Press any key to quit the game: \n")

# game over
game_over()
