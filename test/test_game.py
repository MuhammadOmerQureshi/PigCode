import unittest
from unittest.mock import patch, MagicMock
from game import Game, Player, main


class TestGame(unittest.TestCase):

    @patch(
        "builtins.input", side_effect=["q", "q"]
    )  # Player chooses to quit consecutively
    def test_game_consecutive_quits(self, mock_input):
        first_quit = self.game.get_player_action(self.player1)
        second_quit = self.game.get_player_action(self.player1)
        self.assertEqual(first_quit, "q")
        self.assertEqual(second_quit, "q")

    @patch("builtins.input", side_effect=["h", "r", "q", "r", "h", "r", "q"])
    def test_get_player_action_successive_mixed_actions(self, mock_input):
        actions = [self.game.get_player_action(self.player1) for _ in range(7)]
        self.assertEqual(actions, ["h", "r", "q", "r", "h", "r", "q"])

    @patch("builtins.input", side_effect=["r"])
    def test_get_player_action_roll(self, mock_input):
        action = self.game.get_player_action(self.player1)
        self.assertEqual(action, "r")

    @patch("builtins.input", side_effect=["h"])
    def test_get_player_action_hold(self, mock_input):
        action = self.game.get_player_action(self.player1)
        self.assertEqual(action, "h")

    @patch("builtins.input", side_effect=["q"])
    def test_get_player_action_quit(self, mock_input):
        action = self.game.get_player_action(self.player1)
        self.assertEqual(action, "q")

    @patch("builtins.input", side_effect=["h", "r"])
    def test_get_player_action_multiple(self, mock_input):
        actions = [self.game.get_player_action(self.player1) for _ in range(2)]
        self.assertEqual(actions, ["h", "r"])

    @patch(
        "builtins.input",
        side_effect=["r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r"],
    )
    def test_get_player_action_max_rolls(self, mock_input):
        actions = [self.game.get_player_action(self.player1) for _ in range(11)]
        self.assertEqual(
            actions, ["r", "r", "r", "r", "r", "r", "r", "r", "r", "r", "r"]
        )

    @patch("builtins.input", side_effect=["c"])
    def test_get_player_action_cheat(self, mock_input):
        action = self.game.get_player_action(self.player1)
        self.assertEqual(action, "c")

    @patch("builtins.input", side_effect=["R", "H"])
    def test_get_player_action_mixed_case(self, mock_input):
        actions = [self.game.get_player_action(self.player1) for _ in range(2)]
        self.assertEqual(actions, ["r", "h"])

    def setUp(self):
        self.player1 = Player("Player1")
        self.player2 = Player("Computer", intelligence=True)
        self.players = [self.player1, self.player2]
        self.game = Game(self.players)

    @patch("builtins.input", side_effect=["r", "h"])
    @patch.object(Player, "roll_dice", return_value=5)
    def test_play_turn_human(self, mock_roll, mock_input):
        self.game.play_turn(self.player1)
        self.assertEqual(self.player1.score, 0)

    @patch.object(Player, "decide_hold", return_value=True)
    @patch.object(Player, "roll_dice", return_value=5)
    def test_play_turn_computer(self, mock_roll, mock_hold):
        self.game.play_turn(self.player2)
        self.assertTrue(mock_hold.called)
        self.assertEqual(self.player2.score, 0)

    @patch("builtins.input", side_effect=["q"])
    def test_play_turn_quit_midgame(self, mock_input):
        result = self.game.play_turn(self.player1)
        self.assertEqual(result, "quit")

    @patch("builtins.input", side_effect=["x", "r"])  # 'x' is invalid
    def test_get_player_action_invalid_input(self, mock_input):
        action = self.game.get_player_action(self.player1)
        self.assertEqual(action, "r")

    @patch.object(Game, "play_turn", side_effect=[None, "quit"])
    def test_play_round_quit_after_one_turn(self, mock_play_turn):
        result = self.game.play_round()
        self.assertEqual(result, "quit")

    @patch("builtins.input", side_effect=["r", "r", "h", "q"])
    def test_play_round_player_wins(self, mock_input):
        self.player1.score = 101
        winner = self.game.play_round()
        self.assertEqual(winner.score, 101)

    @patch("builtins.input", side_effect=["Alice", "1", "10", "q"])
    @patch("builtins.print")
    def test_main_game_quit_immediately(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Game has been quit.")

    @patch(
        "builtins.input", side_effect=["Alice", "1", "10", "r", "h", "no"]
    )  # Inputs for one round of gameplay and exit
    @patch("builtins.print")
    def test_main_game_single_complete_round(self, mock_print, mock_input):
        # Mocking the game and player interactions to simulate game flow
        with patch("game.Game") as mock_game_class:
            mock_game = mock_game_class.return_value
            mock_player = MagicMock(
                name="Alice", score=50
            )  # Correctly define MagicMock with unique keyword arguments
            mock_game.play_round.return_value = mock_player
            main()

            # Checking that a round was played
            mock_game.play_round.assert_called()

            # Checking print outputs for expected end of game interactions
            expected_message = (
                f"🏆 {mock_player.name} wins with a score of {mock_player.score}!"
            )
            mock_print.assert_any_call(expected_message)
            mock_print.assert_any_call("Thanks for playing! 🖐️")


if __name__ == "__main__":
    unittest.main()
