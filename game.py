from config_reader import *
from player import *
class Game:
    def __init__(self, config_file : str, soldiers : list) -> None:
        config_reader = ConfigReader(config_file)
        self.map = config_reader.map
        print("Configuration file was loaded")
        self.year = 617
        self.players = [Player(), Player()]
        self.current_turn = 0
    
    def next_player(self):
        self.current_turn += 1
        if self.current_turn == len(self.players):
            self.current_turn = 0
        return self.players[self.current_turn]

    def current_player(self):
        return self.players[self.current_turn]

    def display_map(self):
        print('  X',end='')
        for x in range(self.map.width):
            print("{:02n}".format(x),end="X\n" if x == self.map.width - 1 else " ")

        print(" Y+",end="")
        for x in range(self.map.width):
            print("--".format(x),end="+\n" if x == self.map.width - 1 else "-")

        for y in range(self.map.height):
            print("{:02n}".format(y), end='')
            for x in range(self.map.width):
                loc = (x,y)
                if loc == (1,1):
                    print("|H1",end="")
                elif loc == (3,3):
                    print("|H2",end="")
                elif loc in self.map.resources:
                    res = self.map.resources[loc]
                    print(f"|{res.display()}", end="")
                else:
                    print("|  ", end="")
            print("|")
        print(" Y+",end="")
        for x in range(self.map.width):
            print("--".format(x),end="+\n" if x == self.map.width - 1 else "-")


    def display_price(self):
        print("""
Recruit Prices:
Spearman (S) - 1W, 1F
Archer (A) - 1W, 1G
Knight (K) - 1F, 1G
Scout (T) - 1W, 1F, 1G""")

    def run(self):
        print("game Started: Little Battle! (enter QUIT to quit the game)\n")
        print("Please check the battlefield, commander.")
        self.display_map()
        print("enter DIS to display the map\n")
        self.display_price()
        print("enter PRIS to display the price list\n")
        while True:
            print(f"- Year {self.year}")
            self.main_loop()

    

    def main_loop(self):
        print(f"+++Player {self.current_turn + 1}'s Stage: Recruit Armies+++")
        self.current_player().display_asset()
        if self.current_player().can_recruit():
            self.current_player().recruit()