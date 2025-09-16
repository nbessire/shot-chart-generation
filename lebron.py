import random


class LebronJames:
    def __init__(self):
        self.transition_matrix = {
            "Three": {"Three": 0.3, "Jumper": 0.2, "Drive": 0.3, "FreeThrow": 0.2},
            "Jumper": {"Three": 0.2, "Jumper": 0.1, "Drive": 0.4, "FreeThrow": 0.3},
            "Drive": {"Three": 0.2, "Jumper": 0.1, "Drive": 0.3, "FreeThrow": 0.4},
            "FreeThrow": {"Three": 0.2, "Jumper": 0.1, "Drive": 0.35, "FreeThrow": 0.35},
        }
        self.moves = list(self.transition_matrix.keys())

    def startState(self):
        return random.choice(self.moves)
    
    def generateGame(self, num_shots=20):
        current_move = self.startState()
        return random.choices(
            self.moves,
            weights=[self.transition_matrix[current_move][move] for move in self.moves],
            k=num_shots
        )
        