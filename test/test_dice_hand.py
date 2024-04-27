

import unittest
from unittest.mock import patch
from dice_hand import DiceHand

class TestDiceHand(unittest.TestCase):
    def setUp(self):
        # Create a DiceHand instance for testing
        self.dice_hand = DiceHand()

    @patch('dice.Dice.roll', return_value=3)  # Patch the Dice.roll method
    def test_process_roll(self, mock_roll):
        # Test if process_roll returns a valid roll and updates turn score accordingly
        roll = self.dice_hand.process_roll()
        self.assertEqual(roll, 3)
        self.assertEqual(self.dice_hand.turn_score, 3)

    def test_initial_turn_score(self):
        # Test if the initial turn score is set to 0
        self.assertEqual(self.dice_hand.turn_score, 0)

if __name__ == '__main__':
    unittest.main()
   