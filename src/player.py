from dice_hand import DiceHand

class Player:
    def __init__(self, name, intelligence=None):
        self.original_name = name
        self.name = name
        self.score = 0
        self.dice_hand = DiceHand()
        self.intelligence = intelligence  # None for human players

    def roll_dice(self):
        roll = self.dice_hand.process_roll()
        self.display_roll(roll)
        return roll

    def display_roll(self, roll):
        if roll == 1:
            print(f"{self.name} rolled a 1. 🎲 No points this turn.")
        else:
            print(f"{self.name} rolled a {roll}. 🎲 Turn total: {self.dice_hand.turn_score}")

    def hold(self):
        self.score += self.dice_hand.turn_score
        print(f"{self.name} holds. Total score: {self.score} 📈")
        self.dice_hand.turn_score = 0

    def cheat(self):
        self.score += 20
        print(f"{self.name} uses CHEAT! +20 points! 🚀")

    def reset(self):
        self.score = 0
        self.dice_hand.turn_score = 0

    def decide_hold(self):
        if self.intelligence:
            return self.intelligence.decide_hold(self.dice_hand.turn_score)
        return False
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value