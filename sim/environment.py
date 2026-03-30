import numpy as np

class Environment:
    def __init__(self, config):
        self.size = config.get("size", (10, 10))
        self.objects = []
        self.agent_pos = np.array([0, 0])
        self.step_count = 0
        self.max_steps = config.get("max_steps", 100)

    def reset(self):
        self.agent_pos = np.array([0, 0])
        self.step_count = 0
        return self._get_observation()

    def step(self, action):
        self.step_count += 1

        if action == "move_up":
            self.agent_pos[1] += 1
        elif action == "move_down":
            self.agent_pos[1] -= 1
        elif action == "move_left":
            self.agent_pos[0] -= 1
        elif action == "move_right":
            self.agent_pos[0] += 1

        obs = self._get_observation()
        done = self.step_count >= self.max_steps

        return obs, 0.0, done, {}

    def _get_observation(self):
        return {
            "agent_pos": self.agent_pos.tolist(),
            "visible_objects": self._visible_objects()
        }

    def _visible_objects(self):
        # placeholder for occlusion logic
        return self.objects
