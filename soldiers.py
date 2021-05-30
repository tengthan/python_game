from resource import Resource, Gold, Food, Wood
import math

class Victory(Exception):
    def __init__(self, soldier):
        self.soldier = soldier

class Soldier:
    def __init__(self,type,init_location) -> None:
        self.type=type
        self.location= init_location
        self.moved_this_turn = False

    def is_spearmen(self):
        return self.type == "spearmen" 

    def is_archer(self):
        return self.type == "archer"

    def is_knight(self):
        return self.type == "knight"

    def is_scout(self):
        return self.type == "scout"
    
    def cost(self):
        (0,0,0)

    def verify_the_cost(self, player) -> bool:
        cost = self.cost()
        gold, food, wood = player.gold - cost[0], player.food - cost[1], player.wood - cost[2]
        return gold * food * wood >= 0

    def move(self, dest, map):
        origin_x, origin_y = self.location
        move_length = math.sqrt((dest[0] - origin_x)** 2 + (dest[1] - origin_y)**2)
        if not isinstance(self,Scout) and move_length > 1:
            print("Only Scout can move up to 2 steps per turn. Try again")
            return self.player.move_armies(map)
        if self.moved_this_turn:
            print("This army has been moved, try another one.")
            return self.player.move_armies(map)
        dest_x, dest_y = dest 
        dest_x -= self.location[0]
        dest_x = 0 if not dest_x else dest_x / abs(dest_x)
        dest_y -= self.location[1]
        dest_y = 0 if not dest_y else dest_y / abs(dest_y)
        thing_at_dest = map.thing_at.get(dest)
        if isinstance(thing_at_dest, Soldier) and thing_at_dest.player is self:
            print("Invalid move. Try again.")
            return self.player.move_armies(map)
        for i in range(int(move_length)):
            self.actual_move((dest_x,dest_y), map)

        
    def actual_move(self, direction, map):
        new_location = (self.location[0] + direction[0], self.location[1] + direction[1])
        thing_at_dest = map.thing_at.get(new_location)
        if new_location == self.player.opponent.home_base:
            raise Victory(self)
        elif not thing_at_dest:
            self.update_location(new_location,map)
        elif isinstance(thing_at_dest,Soldier):
            if (self.fight(thing_at_dest) < 0):
                print(f"We lost the army {thing_at.__class__.__name__} due to your command!")
                return thing_at.die(map)
            if self.fight(thing_at_dest) == 0: #same type
                thing_at_dest.die(map)
                self.die(map)
                return print(f"We destroyed the enemy {self.__class__.__name__} with massive loss")
            if self.fight(thing_at_dest):
                thing_at_dest.die(map)
                self.update_location(new_location,map)
                return print(f"Great! We defeated the enemy {thing_at_dest.__class__.__name__}!")
        elif isinstance(thing_at_dest, Resource):
            if thing_at_dest.is_water():
                print(f"We lost the army {self.__class__.__name__} due to your command!")
                return self.die(map) 
            print(f"Good. We collected 2 {thing_at_dest.__class__.__name__}.")
            if thing_at_dest.is_gold():
                self.player.gold += 2
            elif thing_at_dest.is_wood():
                self.player.wood += 2
            elif thing_at_dest.is_food():
                self.player.food += 2
            self.update_location(new_location,map)

    def fight(self, opponent):
        pass

    def die(self,map):
        del map.thing_at[self.location]
        self.player.armies.remove(self)

    def update_location(self,loc,map):
        loc = tuple(int(e) for e in loc)
        map.thing_at[loc] = self
        del map.thing_at[self.location]
        self.location = loc
        self.moved_this_turn = True

class Scout(Soldier):
    def __init__(self, init_location) -> None:
        super().__init__("scout", init_location)

    def cost(self):
        return(
            1, #gold
            1, #food
            1) #wood
        
    def display(self):
        return f"T{self.player_index + 1}"
    
    def fight(self, opp):
        if opp.is_scout():
            return 0
        else:
            return -1

class Knight(Soldier):
    def __init__(self, init_location) -> None:
        super().__init__("Knight", init_location)

    def fight(self, opp):
        if opp.is_knight():
            return 0
        elif opp.is_spearmen():
            return -1 
        else:
            return 1

    def display(self):
        return f"K{self.player_index + 1}"

    def cost(self):
        return(
            1, #gold
            1, #food
            0) #wood

class Spearmen(Soldier):

    def __init__(self, init_location) -> None:
        super().__init__("spearman", init_location)

    def display(self):
        return f"S{self.player_index + 1}"

    def cost(self):
        return(
            0, #gold
            1, #food
            1) #wood

    def fight(self, opp):
        if opp.is_spearmen():
            return 0
        elif opp.is_archer():
            return  -1 
        else:
            return 1

class Archer(Soldier):

    def __init__(self, init_location) -> None:
        super().__init__("archer", init_location)

    def display(self):
        return f"A{self.player_index + 1}"

    def cost(self):
        return(
            1, #gold
            0, #food
            1) #wood

    def fight(self, opp):
        if opp.is_archer():
            return 0
        elif opp.is_knight():
            return  -1
        else:
            return 1