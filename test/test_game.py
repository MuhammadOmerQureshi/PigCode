import unittest
from unittest.mock import patch, MagicMock
from game import Game, Player

class TestGame(unittest.TestCase):
    """def setUp(self):
        # Create player instances for testing
        self.player1 = Player("player1") #give player1 the name player1
        self.player2 = Player("player2") #give player2 the name player2
        self.players = [self.player1, self.player2]
        self.game = Game(self.players)"""

    @patch('builtins.input', side_effect=['r'])
    def test_get_player_action_roll(self, mock_input):
        action = self.game.get_player_action(self.player1)
        self.assertEqual(action, 'r')

    @patch('builtins.input', side_effect=['h'])
    def test_get_player_action_hold(self, mock_input):
        action = self.game.get_player_action(self.player1)
        self.assertEqual(action, 'h')

    @patch('builtins.input', side_effect=['q'])
    def test_get_player_action_quit(self, mock_input):
        action = self.game.get_player_action(self.player1)
        self.assertEqual(action, 'q')

    @patch('builtins.input', side_effect=['h', 'r'])
    def test_get_player_action_multiple(self, mock_input):
        actions = [self.game.get_player_action(self.player1) for _ in range(2)]
        self.assertEqual(actions, ['h', 'r'])

    @patch('builtins.input', side_effect=['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'])
    def test_get_player_action_max_rolls(self, mock_input):
        actions = [self.game.get_player_action(self.player1) for _ in range(11)]
        self.assertEqual(actions, ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'])

    @patch('builtins.input', side_effect=['c'])
    def test_get_player_action_cheat(self, mock_input):
        action = self.game.get_player_action(self.player1)
        self.assertEqual(action, 'c')

    @patch('builtins.input', side_effect=['R', 'H'])
    def test_get_player_action_mixed_case(self, mock_input):
        actions = [self.game.get_player_action(self.player1) for _ in range(2)]
        self.assertEqual(actions, ['r', 'h'])

    def setUp(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Computer", intelligence=True)  # Assuming intelligence is a boolean for simplicity
        self.players = [self.player1, self.player2]
        self.game = Game(self.players)

    @patch('builtins.input', side_effect=['r', 'h'])
    @patch.object(Player, 'roll_dice', return_value=5)  # Assuming roll_dice method returns a dice result
    def test_play_turn_human(self, mock_roll, mock_input):
        self.game.play_turn(self.player1)
        self.assertEqual(self.player1.score, 0)  # Assuming score updates correctly after rolling 5

    @patch.object(Player, 'decide_hold', return_value=True)
    @patch.object(Player, 'roll_dice', return_value=5)
    def test_play_turn_computer(self, mock_roll, mock_hold):
        self.game.play_turn(self.player2)
        self.assertTrue(mock_hold.called)
        self.assertEqual(self.player2.score, 0)

    def play_round(self):
        # This would simulate playing a round
        return MagicMock(name='Player1', score=120)  # Example player who might win
    
    """@patch('builtins.input', side_effect=['r', 'h'])
    @patch.object(Player, 'roll_dice', side_effect=[5, 1])  # Including rolling a 1 to test that path
    def test_play_turn_human_roll_then_one(self, mock_roll, mock_input):
        self.game.play_turn(self.player1)
        self.assertIn(mock_roll.call_count, [2])  # Check if roll_dice was called twice"""

    @patch('builtins.input', side_effect=['q'])
    def test_play_turn_quit_midgame(self, mock_input):
        result = self.game.play_turn(self.player1)
        self.assertEqual(result, "quit")

    @patch('builtins.input', side_effect=['x', 'r'])  # 'x' is invalid
    def test_get_player_action_invalid_input(self, mock_input):
        action = self.game.get_player_action(self.player1)
        self.assertEqual(action, 'r')

    @patch.object(Game, 'play_turn', side_effect=[None, "quit"])
    def test_play_round_quit_after_one_turn(self, mock_play_turn):
        result = self.game.play_round()
        self.assertEqual(result, "quit")
    
    @patch('builtins.input', side_effect=['r', 'r', 'h', 'q'])
    def test_play_round_player_wins(self, mock_input):
        self.player1.score = 101  # Manually set the player's score to a winning score
        winner = self.game.play_round()
        self.assertEqual(winner.score, 101)


    def main(self):
        self.players = self.setup_game()
        while True:
            winner = self.play_round()
            if winner == "quit":
                print("Game has been quit.")
                break
            elif winner:
                print(f"🏆 {winner.name} wins with a score of {winner.score}!")
            if input("Do you want to play again? (yes/no): ").lower().strip() != 'yes':
                print("Thanks for playing! 🖐️")
                break

if __name__ == '__main__':
    unittest.main()
