class HighScore:
    def __init__(self, histogram):
        self.histogram = histogram

    def update_highscore(self, player):
        self.histogram.update_highscore(player)