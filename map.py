from resource import Resource, Wood, Food, Gold
from soldiers import *
class Map:
    def __init__(self, size,water_locations, wood_locations, food_loacations, gold_locations):
        self.resources = {}
        self.thing_at = self.resource
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
        if isinstance(self.thing_at.get(loc),Soldier):
            pass
