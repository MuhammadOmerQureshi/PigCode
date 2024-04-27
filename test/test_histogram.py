import unittest
from unittest.mock import patch, mock_open
from histogram import Histogram

class TestHistogram(unittest.TestCase):
    def setUp(self):
        # Apply a global mock to ensure all file reads return an empty JSON object.
        # This handles the constructor call inside every test that doesn't explicitly patch the open.
        self.mock_file = mock_open(read_data='{}')
        self.patcher = patch('builtins.open', self.mock_file)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_load_highscores_existing_file(self):
        # Overriding the default setup for specific test data
        with patch('builtins.open', mock_open(read_data='{"Jane Doe": {"name": "Jane Doe", "best_score": 95, "games_played": 1}}')) as mock_file:
            histogram = Histogram(filename="test_highscore.json")
            highscores = histogram.load_highscores()
            self.assertEqual(highscores['Jane Doe']['best_score'], 95)

    def test_load_highscores_non_existing_file(self):
        # This should use the default empty JSON setup from setUp
        histogram = Histogram(filename="test_highscore.json")
        highscores = histogram.load_highscores()
        self.assertEqual(highscores, {})


    @patch('json.dump')
    def test_save_highscores(self, mock_json_dump):
        histogram = Histogram(filename="test_highscore.json")
        histogram.highscores = {"John Doe": {"name": "John Doe", "best_score": 120, "games_played": 2}}
        histogram.save_highscores()
        self.mock_file.assert_called_with("test_highscore.json", "w")
        mock_json_dump.assert_called_with(histogram.highscores, self.mock_file(), indent=4)

if __name__ == '__main__':
    unittest.main()
