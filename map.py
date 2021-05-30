from resource import Resource, Wood, Food, Gold
from soldiers import *
class Map:
    def __init__(self, size,water_locations, wood_locations, food_loacations, gold_locations):
        self.resources = {}
        self.thing_at = self.resources
        self.width, self.height = size
        for w in water_locations:
            self.resources[w] = Resource("water")
        for w in wood_locations:
            self.resources[w] = Wood()
        for f in food_loacations:
            self.resources[f] = Food()
        for g in gold_locations:
            self.resources[g] = Gold()

    def is_occupied(self,loc):
        return isinstance(self.thing_at.get(loc),Soldier)
    
    def is_next_to_the_home_base(self,player,loc):
        return loc in [
            (player.home_base[0], player.home_base[1]-1),
            (player.home_base[0] + 1, player.home_base[1]),
            (player.home_base[0], player.home_base[1] + 1),
            (player.home_base[0] - 1, player.home_base[1])
        ]

    def can_place_army(self,player):
        for loc in [
            (player.home_base[0], player.home_base[1]-1),
            (player.home_base[0] + 1, player.home_base[1]),
            (player.home_base[0], player.home_base[1] + 1),
            (player.home_base[0] - 1, player.home_base[1])
        ]:
            if not self.thing_at.get(loc):
                return True 
        return False

    def display_map(self):
        print('  X',end='')
        for x in range(self.width):
            print("{:02n}".format(x),end="X\n" if x == self.width - 1 else " ")

        print(" Y+",end="")
        for x in range(self.width):
            print("--".format(x),end="+\n" if x == self.width - 1 else "-")

        for y in range(self.height):
            print("{:02n}".format(y), end='')
            for x in range(self.width):
                loc = (x,y)
                if loc == (1,1):
                    print("|H1",end="")
                elif loc == (3,3):
                    print("|H2",end="")
                elif loc in self.resources:
                    res = self.thing_at[loc]
                    print(f"|{res.display()}", end="")
                else:
                    print("|  ", end="")
            print("|")
        print(" Y+",end="")
        for x in range(self.width):
            print("--".format(x),end="+\n" if x == self.width - 1 else "-")  
                                                                             