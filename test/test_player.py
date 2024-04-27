import unittest
from unittest.mock import patch
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Create a player
        self.player = Player("player1")

    def test_roll_dice(self):
        # Test if roll_dice returns a valid roll
        with patch.object(self.player.dice_hand, 'process_roll', return_value=4):
            roll = self.player.roll_dice()
        self.assertEqual(roll, 4)

    @patch('builtins.print')
    def test_display_roll(self, mock_print):
        # Test if display_roll prints correct message
        self.player.display_roll(2)
        mock_print.assert_called_once_with("player1 rolled a 2. 🎲 Turn total: 0")

    @patch('builtins.print')
    def test_hold(self, mock_print):
        # Test if hold updates player's score correctly
        self.player.dice_hand.turn_score = 10
        self.player.hold()
        self.assertEqual(self.player.score, 10)

    @patch('builtins.print')
    def test_cheat(self, mock_print):
        # Test if cheat increases player's score by 20
        self.player.cheat()
        self.assertEqual(self.player.score, 20)

    def test_reset(self):
        # Test if reset sets player's score and turn_score to 0
        self.player.score = 30
        self.player.dice_hand.turn_score = 15
        self.player.reset()
        self.assertEqual(self.player.score, 0)
        self.assertEqual(self.player.dice_hand.turn_score, 0)

    def test_decide_hold(self):
        # Test if decide_hold returns False for human player
        self.assertFalse(self.player.decide_hold())

if __name__ == '__main__':
    unittest.main()
