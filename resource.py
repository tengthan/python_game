
class Resource:
    def __init__(self, type) -> None:
        self.type = type

    def is_water(self):
        return self.type == "water"

    def is_food(self):
        return self.type  == "food"

    def is_gold(self):
        return self.type == "gold"

    def is_wood(self):
        return self.type == "wood"

    def __eq__(self, o: object) -> bool:
        return self.type == o.type
    
    def display(self):
        return "~~"


class Food(Resource):
    def __init__(self) -> None:
        Resource.__init__(self,"food")

    def display(self):
        return "FF"

class Gold(Resource):
    def __init__(self) -> None:
        Resource.__init__(self,"gold")

    def display(self):
        return "GG"

class Wood(Resource):
    def __init__(self) -> None:
        Resource.__init__(self,"wood")

    def display(self):
        return "WW"
