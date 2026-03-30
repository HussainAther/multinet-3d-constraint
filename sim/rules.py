class FragileRule:
    def __init__(self):
        self.violations = 0

    def check(self, action, obj):
        if obj.get("type") == "fragile" and action == "move":
            self.violations += 1
            return True
        return False
