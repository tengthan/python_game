def e_int(i, line_name = None):
    i = int(i)
    if i > 7 or i < 5:
        raise ArithmeticError("Invalid Configuration File: width and height should range from 5 to 7!")
    return i

def e_ni_int(i, line_name = None):
    #i = int(i)
    try:
        return int(i)
    except SyntaxError:
        raise 
    except ValueError:
        raise ValueError(f"e Invalid Configuration File: line {line_name} contains non integer characters!")

def check_out_of_the_map(map_size, positions, line_name = None):
    for p in positions:
        if p[0] < 0 or p[1] < 0 or p[0] > map_size[0]-1 or p[1] > map_size[1]-1 :
            raise ArithmeticError(f"e Invalid Configuration File: line {line_name} contains a position that is out of map.")

def check_if_on_reversed_locations(p, locations):
    if p in locations:
        raise ValueError("e Invalid Configuration File: The positions of home bases or the positions next to the home bases are occupied!")
