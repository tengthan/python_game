from config_reader import *
from player import Player
class Game:
    def __init__(self, config_file : str, soldiers : list) -> None:
        config_reader = ConfigReader(config_file)
        self.map = config_reader.map
        print("Configuration file was loaded")
        self.year = 617
        self.players = [Player((1,1)), Player((3,3))]
        for i in range(len(self.players)):
            self.players[i].index = i
        self.current_turn = 0
    
    def next_player(self):
        self.current_turn += 1
        if self.current_turn == len(self.players):
            self.current_turn = 0
        return self.players[self.current_turn]

    def current_player(self):
        return self.players[self.current_turn]


    def display_price():
        print("""
Recruit Prices:
Spearman (S) - 1W, 1F
Archer (A) - 1W, 1G
Knight (K) - 1F, 1G
Scout (T) - 1W, 1F, 1G""")

    def run(self):
        print("game Started: Little Battle! (enter QUIT to quit the game)\n")
        print("Please check the battlefield, commander.")
        self.map.display_map()
        print("enter DIS to display the map\n")
        Game.display_price()
        print("enter PRIS to display the price list\n")
        while True:
            print(f"- Year {self.year}")
            self.main_loop()


    def main_loop(self):
        print(f"+++Player {self.current_turn + 1}'s Stage: Recruit Armies+++")
        self.current_player().display_asset()
        if self.current_player().can_recruit():
            self.current_player().recruit(self.map)
        self.current_player().move_armies(self.map)