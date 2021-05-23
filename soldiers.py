from resource import Resource, Gold, Food, Wood
class Soldier:
    def __init__(self,type,init_location) -> None:
        self.type=type
        self.location= init_location

    def is_spearmen(self):
        return self.type == "spearmen" 

    def is_archer(self):
        return self.type == "archer"

    def is_knight(self):
        return self.type == "knight"

    def is_scout(self):
        return self.type == "scout"

    def move(self,direction,steps = 1):
        if not self.is_scout() and steps >1: 
            print("do nothing")
            return 
        elif self.is_scout() and steps > 2:
            return 
        for step in steps:
           self.location=(self.location[0]+direction[0],self.location[1]+direction[1])
    
    def cost(self):
        pass

class Scout(Soldier):
    def __init__(self, init_location) -> None:
        super().__init__("scout", init_location)

    def cost(self):
        return(Gold(),Food(),Wood())

class Knight(Soldier):
    def __init__(self, init_location) -> None:
        super().__init__("Knight", init_location)

    def cost(self):
        return(Food(),Gold())

class Spearmen(Soldier):

    def __init__(self, init_location) -> None:
        super().__init__("spearman", init_location)

    def cost(self):
        return(Food(),Wood())

class Archer(Soldier):

    def __init__(self, init_location) -> None:
        super().__init__("archer", init_location)

    def cost(self):
        return(Wood(),Gold()) 

