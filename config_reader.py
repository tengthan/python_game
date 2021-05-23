from os import path
from defs import *
from map import Map
class ConfigReader:
  def __init__(self,filepath):

    if not filepath:
        print("Usage: python3 little_battle.py <filepath>")
        return

    if not path.isfile(filepath):
        raise FileNotFoundError(f"Could not find file located at {filepath}")

    file_content=open(filepath,"r").readlines()
    
    line = file_content[0].split()[1].split('x')
    try:    
        self.map_size = [e_int(i) for i in line]
    except:
        raise SyntaxError("Invalid Configuration File: frame should be in format widthxheight!")
    
    reversed_locations = [
        (1,1),(self.map_size[0]-2,self.map_size[1]-2),
         (0, 1), (1, 0), (2, 1), (1, 2),
         (self.map_size[0]-3,self.map_size[1]-2),
         (self.map_size[0]-2,self.map_size[1]-3),
         (self.map_size[0]-1,self.map_size[1]-2),
         (self.map_size[0]-2,self.map_size[1]-1)
    ]

    water_raw_locations = [e_ni_int(i, "Water") for i in file_content[1].split()[1:]]
    
    if len(water_raw_locations) % 2:
        raise SyntaxError("e Invalid Configuration File: line Water has an odd number of elements!")
    self.water_locations = []
    while water_raw_locations:
        p = (water_raw_locations.pop(0), water_raw_locations.pop(0))
        check_if_on_reversed_locations(p, reversed_locations)
        self.water_locations.append(
            p
        )
    check_out_of_the_map(self.map_size,self.water_locations, "Water")


    wood_raw_locations = [e_ni_int(i, "Wood") for i in file_content[2].split()[1:]]
    if len(wood_raw_locations) % 2:
        raise SyntaxError("e Invalid Configuration File: line Wood has an odd number of elements!")
    self.wood_locations = []
    while wood_raw_locations:
        p = (wood_raw_locations.pop(0), wood_raw_locations.pop(0))
        check_if_on_reversed_locations(p, reversed_locations)
        self.wood_locations.append(
            p
        )
    check_out_of_the_map(self.map_size,self.wood_locations, "Wood")
    
    food_raw_locations = [e_ni_int(i, "Food") for i in file_content[3].split()[1:]]
    if len(food_raw_locations) % 2:
        raise SyntaxError("e Invalid Configuration File: line Food has an odd number of elements!")
    self.food_locations = []
    while food_raw_locations:
        p = (food_raw_locations.pop(0), food_raw_locations.pop(0))
        check_if_on_reversed_locations(p, reversed_locations)
        self.food_locations.append(
            p
        )
    check_out_of_the_map(self.map_size,self.food_locations, "Food")

    gold_raw_locations = [e_ni_int(i, "Gold") for i in file_content[4].split()[1:]]
    if len(gold_raw_locations) % 2:
        raise SyntaxError("e Invalid Configuration File: line Gold has an odd number of elements!")
    self.gold_locations = []
    while gold_raw_locations:
        p = (gold_raw_locations.pop(0), gold_raw_locations.pop(0))
        check_if_on_reversed_locations(p, reversed_locations)
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

    self.map = Map(
        self.map_size,
        self.water_locations,
        self.wood_locations,
        self.food_locations,
        self.gold_locations
    )
    