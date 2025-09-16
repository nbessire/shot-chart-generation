import random


class StephCurry:
    def __init__(self):
        self.transition_matrix = {
            "Three": {"Three": 0.6, "Jumper": 0.1, "Drive": 0.2, "FreeThrow": 0.1},
            "Jumper": {"Three": 0.45, "Jumper": 0.2, "Drive": 0.25, "FreeThrow": 0.1},
            "Drive": {"Three": 0.4, "Jumper": 0.1, "Drive": 0.2, "FreeThrow": 0.3},
            "FreeThrow": {"Three": 0.7, "Jumper": 0.1, "Drive": 0.1, "FreeThrow": 0.1},
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
        