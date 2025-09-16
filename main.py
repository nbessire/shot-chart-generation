from curry import StephCurry
from durant import KevinDurant
from lebron import LebronJames
import matplotlib.pyplot as plt
from PIL import Image


def main():
    name = input("Enter your choice of players (Curry, Lebron, Durant): ").strip().lower()
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
    frequencies = {"Three": 0, "Jumper": 0, "Drive": 0, "FreeThrow": 0}
    for shot in game_sequence:
        frequencies[shot] += 1
    points = player.estimatedPoints(frequencies)

    court = Image.open("court.png")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(court)
    ax.axis("off")

    fig.suptitle(f"{name} - Predicted Points: {points:.1f}", fontsize=16)

    labelPos = {
        "Three": (400, 475),
        "FreeThrow": (400, 360),
        "Jumper": (580, 330),
        "Drive": (404, 175),
    }

    for shot, (x, y) in labelPos.items():
        ax.text(
            x,
            y,
            f"{shot}: {frequencies[shot]}",
            fontsize=12,
            color="white",
            ha="center",
            va="center",
            bbox=dict(facecolor="black", alpha=0.5, boxstyle="round,pad=0.3"),
        )

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()






    
