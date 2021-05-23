from genericpath import isfile
import sys
from os import path, remove
from typing import List
# from typing_extensions import ParamSpecArgs
from defs import *
from config_reader import *
from game import *
from map import *
from player import *
from soldiers import *

if __name__ == "__main__":
    game = Game("config.txt", [])
    game.run()