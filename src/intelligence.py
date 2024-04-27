class Intelligence:
    def __init__(self, threshold=20):
        self.threshold = threshold

    def decide_hold(self, turn_score):
        return turn_score >= self.threshold