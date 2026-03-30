import random

class RandomAgent:
    def act(self, observation):
        return random.choice([
            "move_up",
            "move_down",
            "move_left",
            "move_right"
        ])
