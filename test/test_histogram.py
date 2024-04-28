import unittest
from unittest.mock import MagicMock, patch, call, mock_open
from histogram import Histogram


class TestHistogram(unittest.TestCase):
    def setUp(self):
        # Apply a global mock to ensure all file reads return an empty JSON object.
        # This handles the constructor call inside every test that doesn't explicitly patch the open.
        self.mock_file = mock_open(read_data="{}")
        self.patcher = patch("builtins.open", self.mock_file)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_load_highscores_existing_file(self):
        # Overriding the default setup for specific test data
        with patch(
            "builtins.open",
            mock_open(
                read_data='{"Jane Doe": {"name": "Jane Doe", "best_score": 95, "games_played": 1}}'
            ),
        ) as mock_file:
            histogram = Histogram(filename="test_highscore.json")
            highscores = histogram.load_highscores()
            self.assertEqual(highscores["Jane Doe"]["best_score"], 95)

    def test_load_highscores_non_existing_file(self):
        # This should use the default empty JSON setup from setUp
        histogram = Histogram(filename="test_highscore.json")
        highscores = histogram.load_highscores()
        self.assertEqual(highscores, {})

    @patch("json.dump")
    def test_save_highscores(self, mock_json_dump):
        histogram = Histogram(filename="test_highscore.json")
        histogram.highscores = {
            "John Doe": {"name": "John Doe", "best_score": 120, "games_played": 2}
        }
        histogram.save_highscores()
        self.mock_file.assert_called_with("test_highscore.json", "w")
        mock_json_dump.assert_called_with(
            histogram.highscores, self.mock_file(), indent=4
        )

    def test_update_highscore_new_player(self):
        player = MagicMock()
        player.original_name = "Alice"
        player.name = "Alice"
        player.score = 50
        histogram = Histogram(filename="test_highscore.json")
        histogram.update_highscore(player)
        self.assertEqual(histogram.highscores["Alice"]["best_score"], 50)
        self.assertEqual(histogram.highscores["Alice"]["games_played"], 1)

    def test_update_highscore_existing_player_improved_score(self):
        with patch(
            "builtins.open",
            mock_open(
                read_data='{"Bob": {"name": "Bob", "best_score": 30, "games_played": 2}}'
            ),
        ):
            player = MagicMock()
            player.original_name = "Bob"
            player.name = "Bob"
            player.score = 40
            histogram = Histogram(filename="test_highscore.json")
            histogram.update_highscore(player)
            self.assertEqual(histogram.highscores["Bob"]["best_score"], 40)
            self.assertEqual(histogram.highscores["Bob"]["games_played"], 3)

    def test_update_highscore_existing_player_lower_score(self):
        with patch(
            "builtins.open",
            mock_open(
                read_data='{"Charlie": {"name": "Charlie", "best_score": 80, "games_played": 1}}'
            ),
        ):
            player = MagicMock()
            player.original_name = "Charlie"
            player.name = "Charlie"
            player.score = 60
            histogram = Histogram(filename="test_highscore.json")
            histogram.update_highscore(player)
            self.assertEqual(histogram.highscores["Charlie"]["best_score"], 80)
            self.assertEqual(histogram.highscores["Charlie"]["games_played"], 2)

    @patch("builtins.print")
    def test_display_highscores(self, mock_print):
        histogram = Histogram(filename="test_highscore.json")
        histogram.highscores = {
            "Dave": {"name": "Dave", "best_score": 90, "games_played": 4}
        }
        histogram.display_highscores()
        mock_print.assert_called_once_with("Dave - Best Score: 90, Games Played: 4")


if __name__ == "__main__":
    unittest.main()
