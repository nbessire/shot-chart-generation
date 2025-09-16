from curry import StephCurry

def main():
    player = input("Enter your choice of players (Curry, Lebron, Durant): ").strip.lower()
    if player == "curry":
        curry = StephCurry()
        game_sequence = curry.generateGame()
    if player == "lebron":
        pass
    if player == "durant":
        pass
    