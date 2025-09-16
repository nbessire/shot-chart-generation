import random


class KevinDurant:
    def __init__(self):
        self.transition_matrix = {
            "Three": {"Three": 0.2, "Jumper": 0.5, "Drive": 0.2, "FreeThrow": 0.1},
            "Jumper": {"Three": 0.15, "Jumper": 0.5, "Drive": 0.2, "FreeThrow": 0.15},
            "Drive": {"Three": 0.1, "Jumper": 0.4, "Drive": 0.2, "FreeThrow": 0.3},
            "FreeThrow": {"Three": 0.3, "Jumper": 0.3, "Drive": 0.2, "FreeThrow": 0.2},
        }
        self.moves = list(self.transition_matrix.keys())

    def startState(self):
        return random.choice(self.moves)
    
    def generateGame(self, num_shots=18):
        current_move = self.startState()
        return random.choices(
            self.moves,
            weights=[self.transition_matrix[current_move][move] for move in self.moves],
            k=num_shots
        )
    
    def estimatedPoints(self, shotDistribution):
        pointsMap = {"Three": .437 * 3, "Jumper": .52 * 2, "Drive": .823 * 2, "FreeThrow": .882}
        return sum(pointsMap[shot] for shot in shotDistribution)