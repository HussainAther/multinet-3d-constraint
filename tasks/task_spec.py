class TaskSpec:
    def __init__(self, goal, target, constraints):
        self.goal = goal
        self.target = target
        self.constraints = constraints

    def to_dict(self):
        return {
            "goal": self.goal,
            "target": self.target,
            "constraints": self.constraints
        }
