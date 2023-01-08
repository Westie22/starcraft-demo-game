# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Create Marine : attack unit, solder, ability of shooting

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} unit is created.")
        print(f"Strength {hp}, Lvl. of attacking {damage}")


marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 35)