from soldiers import Archer, Knight, Scout, Spearmen
import game

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
        if user_input.lower() == 'quit':
            quit(0)
        elif user_input.lower() == 's':
            self.do_recruit(Spearmen,map)
        elif user_input.lower() == 'a':
            self.do_recruit(Archer,map)
        elif user_input.lower() == 'k':
            self.do_recruit(Knight,map)
        elif user_input.lower() == 't':
            self.do_recruit(Scout,map)
        elif user_input.lower() != 'no':
            print("Sorry, invalid input. Try again.")
            self.recruit(map)

    def move_armies(self,map):
        print("===Player X's Stage: Move Armies===")
        if not self.armies:
            return print("No Army to Move: next turn.")
        map.display_map()
        user_input = input("k Enter four integers as a format ‘x0 y0 x1 y1’ to represent move unit from (x0, y0) to (x1, y1) or 'NO’ to end this turn.\n")

    def do_recruit(self,type_of_soldier,map):
        user_input = input(f"You want to recruit a {type_of_soldier.__name__}. Enter two integers as format ‘x y’ to place your army.\n")
        if user_input.lower() == "dis":
            map.display_map()
            return self.do_recruit(type_of_soldier,map)
        elif user_input.lower() == "pris":
            game.Game.display_price()
            return self.do_recruit(type_of_soldier,map)
        elif user_input.lower() == 'quit':
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
        self.armies.append(new_soldier)

    def display_asset(self):
        print(f"[Your Asset: Wood - {self.wood} Food - {self.food} Gold - {self.gold}]")

    def can_recruit(self):
        return (self.wood * self.food) or \
            (self.wood * self.gold) or \
            (self.food * self.gold) 