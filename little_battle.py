from genericpath import isfile
import sys
from os import path, remove
from typing import List
# from typing_extensions import ParamSpecArgs
from game import Game

if __name__ == "__main__":
    game = Game("config.txt", [])
    game.run()