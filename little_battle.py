from genericpath import isfile
import sys
from os import path, remove

def e_int(i, line_name = None):
    i = int(i)
    if i > 7 or i < 5:
        raise ArithmeticError("Invalid Configuration File: width and height should range from 5 to 7!")
    return i

def e_ni_int(i, line_name = None):
    i = int(i)
    try:
        if i % 2:
            raise SyntaxError(f"e Invalid Configuration File: line {line_name} has an odd number of elements!")
        return i
    except SyntaxError:
        raise 
    except ValueError:
        raise ValueError(f"e Invalid Configuration File: line {line_name} contains non integer characters!")

def check_out_of_the_map(map_size, positions, line_name = None):
    for p in positions:
        if p[0] < 0 or p[1] < 0 or p[0] > map_size[0]-1 or p[1] > map_size[1]-1 :
            raise ArithmeticError(f"e Invalid Configuration File: line {line_name} contains a position that is out of map.")

reversed_locations = [
    (1,1),
    (2,2),
    (0, 1), (1, 0), (2, 1), (1, 2), (3,2),
    (2 , 3), (1,2), (2,1)
]

def check_if_on_reversed_locations(p):
    if p in reversed_locations:
        raise ValueError("e Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied!")

class ConfigReader:
  def __init__(self,filepath):

    if not filepath:
        print("Usage: python3 little_battle.py <filepath>")
        return

    if not path.isfile(filepath):
        raise FileNotFoundError(f"Could not find file located at {filepath}")

    file_content=open(filepath,"r").readlines()
    
    try:
        self.map_size = [e_int(i) for i in file_content[0].split()[1].split('x')]
    except:
        raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight!")
    
    water_raw_locations = [e_ni_int(i, "Water") for i in file_content[1].split()[1:]]
    self.water_locations = []
    while water_raw_locations:
        p = (water_raw_locations.pop(0), water_raw_locations.pop(0))
        check_if_on_reversed_locations(p)
        self.water_locations.append(
            p
        )
    check_out_of_the_map(self.map_size,self.water_locations, "Water")


    wood_raw_locations = [e_ni_int(i, "Wood") for i in file_content[2].split()[1:]]
    self.wood_locations = []
    while wood_raw_locations:
        p = (wood_raw_locations.pop(0), wood_raw_locations.pop(0))
        check_if_on_reversed_locations(p)
        self.wood_locations.append(
            p
        )
    check_out_of_the_map(self.map_size,self.wood_locations, "Wood")
    
    food_raw_locations = [e_ni_int(i, "Food") for i in file_content[3].split()[1:]]
    self.food_locations = []
    while food_raw_locations:
        p = (food_raw_locations.pop(0), food_raw_locations.pop(0))
        check_if_on_reversed_locations(p)
        self.food_locations.append(
            p
        )
    check_out_of_the_map(self.map_size,self.food_locations, "Food")

    gold_raw_locations = [e_ni_int(i, "Gold") for i in file_content[4].split()[1:]]
    self.gold_locations = []
    while gold_raw_locations:
        p = (gold_raw_locations.pop(0), gold_raw_locations.pop(0))
        check_if_on_reversed_locations(p)
        self.gold_locations.append(
            p    
        )
    check_out_of_the_map(self.map_size,self.gold_locations, "Gold")
    all_resources = [*self.gold_locations, * self.food_locations, *self.wood_locations, *self.water_locations]
    uniq_all_res = set(all_resources)
    for i in uniq_all_res:
        all_resources.remove(i)
    if all_resources:
        raise SyntaxError(f"Invalid Configuration File: Duplicate position ({all_resources[0][0]}, {all_resources[0][1]})!")

cfg_reader = ConfigReader("config.txt")
print(cfg_reader.map_size)