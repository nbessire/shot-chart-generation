from curry import StephCurry
from lebron import LebronJames

def main():
    name = input("Enter your choice of players (Curry, Lebron, Durant): ").strip.lower()
    if name == "curry":
        player = StephCurry()
    elif name == "lebron":
        player = LebronJames()
    elif name == "durant":
        player = KevinDurant()
    else:
        print("Player not valid")
        return
    game_sequence = player.generateGame()
    