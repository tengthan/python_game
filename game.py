from config_reader import *
from player import Player
from soldiers import Victory
class Game:
    def __init__(self, config_file : str, soldiers : list) -> None:
        config_reader = ConfigReader(config_file)
        self.map = config_reader.map
        print("Configuration file was loaded")
        self.year = 617
        self.players = [Player((1,1)), Player((3,3))]
        for i in range(len(self.players)):
            self.players[i].index = i
        self.players[0].opponent, self.players[1].opponent = self.players[1], self.players[0]
        self.players[0].home_base = (1,1)
        self.players[1].home_base = (self.map.width - 2, self.map.height - 2)
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
        try:
            while True:
                print(f"- Year {self.year}")
                self.do_this_turn() #first player's turn
                self.do_this_turn() #second player's turn
                self.year += 1
        except Victory as victory:
            soldier = victory.soldier
            print(f"The army {soldier.__class__.__name__} captured the enemy’s capital.")
            user_name = input("What’s your name, commander?")
            print(f"***Congratulation! Emperor <name> unified the country in {self.year}.***")

    def do_this_turn(self):
        print(f"+++Player {self.current_turn + 1}'s Stage: Recruit Armies+++")
        self.current_player().display_asset()
        if self.current_player().can_recruit():
            self.current_player().recruit(self.map)
        while not self.current_player().all_moved():
            if self.current_player().move_armies(self.map) == "not_move":
                break
        for soldier in self.current_player().armies:
            soldier.moved_this_turn = False
        self.next_player()
        