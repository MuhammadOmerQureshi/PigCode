from dice import Dice


class DiceHand:
    def __init__(self):
        self.turn_score = 0

    def process_roll(self):
        roll = Dice.roll()
        if roll == 1:
            self.turn_score = 0
        else:
            self.turn_score += roll
        return roll
