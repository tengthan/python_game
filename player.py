from soldiers import Archer, Knight, Scout, Spearmen, Soldier
from resource import Resource
import game
import math 

class Player:

    def __init__(self, home_base) -> None:
        self.home_base = home_base
        self.gold = 2
        self.wood = 2
        self.food = 2
        self.armies = []

    def recruit(self,map):
        if not map.can_place_army(self):
            return print("No place to recruit new armies.")
        user_input = input("Which type of army to recruit, (enter) ‘S’, ‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage.\n")
        if user_input == 'QUIT':
            quit(0)
        elif user_input == 'S':
            self.do_recruit(Spearmen,map)
        elif user_input == 'A':
            self.do_recruit(Archer,map)
        elif user_input == 'K':
            self.do_recruit(Knight,map)
        elif user_input == 'T':
            self.do_recruit(Scout,map)
        elif user_input == "DIS":
            map.display_map()
            return self.recruit(map)
        elif user_input == "PRIS":
            game.Game.display_price()
            return self.recruit(map)
        elif user_input == "QUIT":
            quit(0)
        elif user_input != 'NO’':
            print("Sorry, invalid input. Try again.")
            self.recruit(map)

    def move_armies(self,map):
        print(f"===Player {self.index + 1}'s Stage: Move Armies===")
        if not self.armies:
            return print("No Army to Move: next turn.")
        map.display_map()
        user_input = input("k Enter four integers as a format ‘x0 y0 x1 y1’ to represent move unit from (x0, y0) to (x1, y1) or 'NO’ to end this turn.\n")
        if user_input == "DIS":
            map.display_map()
            return self.move_armies(map)
        elif user_input == "PRIS":
            game.Game.display_price()
            return self.move_armies(map)
        elif user_input == "QUIT":
            quit(0)
        elif user_input == "NO’":
            return "not_move"
        try:
            user_input = [int(i) for i in user_input.split()]
        except ValueError:
            user_input = []
        if len(user_input) != 4:
            print("Invalid move. Try again.")
            return self.move_armies(map)
        print(tuple(user_input[2:2]))
        self.do_move(
            tuple(user_input[:2]),
            tuple(user_input[2:]),
            map
        )

    def do_move(self,start_loc, dest, map):
        thing_at = map.thing_at[start_loc]
        if not isinstance(thing_at, Soldier):
            print("Invalid move. Try again.")
            return self.move_armies(map)
        dest_x, dest_y = dest 
        if dest_x < 0 or dest_x > map.width - 1 or dest_y < 0 or dest_y > map.height - 1:
            print("Invalid move. Try again.")
            return self.move_armies(map)
        if start_loc == dest:
            print("Invalid move. Try again.")
            return self.move_armies(map)
        
        thing_at.move(dest,map)

    def all_moved(self):
        return len([s for s in self.armies if s.moved_this_turn]) == len(self.armies)

    def do_recruit(self,type_of_soldier,map):
        user_input = input(f"You want to recruit a {type_of_soldier.__name__}. Enter two integers as format ‘x y’ to place your army.\n")
        if user_input == "DIS":
            map.display_map()
            return self.do_recruit(type_of_soldier,map)
        elif user_input == "PRIS":
            game.Game.display_price()
            return self.do_recruit(type_of_soldier,map)
        elif user_input == 'QUIT':
            quit(0)
        try:
            user_input = [int(i) for i in user_input.split(" ")]
            if len(user_input) != 2:
                raise ValueError()
            user_input = tuple(user_input)
        except ValueError:
            print("Sorry, invalid input. Try again.")
            return self.do_recruit(type_of_soldier,map)
        if not map.is_next_to_the_home_base(self,user_input) or map.is_occupied(user_input): 
            print("You must place your newly recruited unit in an unoccupied position next to your home base. Try again.")
            return self.do_recruit(type_of_soldier,map)
        new_soldier = type_of_soldier(user_input)
        if not new_soldier.verify_the_cost(self):
            print("Insufficient resources. Try again.")
            return self.recruit(map)

        self.gold -= new_soldier.cost()[0]
        self.food -= new_soldier.cost()[1]
        self.wood -= new_soldier.cost()[2]

        map.thing_at[user_input] = new_soldier
        new_soldier.player_index = self.index
        new_soldier.player = self
        self.armies.append(new_soldier)
        

    def display_asset(self):
        print(f"[Your Asset: Wood - {self.wood} Food - {self.food} Gold - {self.gold}]")

    def can_recruit(self):
        return (self.wood * self.food) or \
            (self.wood * self.gold) or \
            (self.food * self.gold)  