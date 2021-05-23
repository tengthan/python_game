class Player:

    def __init__(self) -> None:
        self.gold = 2 
        self.wood = 2
        self.food = 2

    def recruit(self):
        user_input = input("Which type of army to recruit, (enter) ‘S’, ‘A’, ‘K’, or ‘T’? Enter ‘NO’ to end this stage.")
        if user_input.lower() == 'quit':
            quit(0)
        elif user_input.lower() == 's':
            pass
        elif user_input.lower() == 'a':
            pass
        elif user_input.lower() == 'k':
            pass
        elif user_input.lower() == 't':
            pass
        elif user_input.lower() != 'no':
            print("Sorry, invalid input. Try again.")
            self.recruit()

    def display_asset(self):
        print(f"[Your Asset: Wood - {self.wood} Food - {self.food} Gold - {self.gold}]")

    def can_recruit(self):
        return (self.wood * self.food) or \
            (self.wood * self.gold) or \
            (self.food * self.gold) 