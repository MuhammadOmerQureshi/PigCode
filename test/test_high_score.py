import unittest
from unittest.mock import MagicMock
from high_score import HighScore

class TestHighScore(unittest.TestCase):
    def setUp(self):
        # Create a mock histogram object
        self.mock_histogram = MagicMock()

        # Create a HighScore instance for testing
        self.highscore = HighScore(self.mock_histogram)

    def test_update_highscore(self):
        # Create a mock player object
        mock_player = MagicMock()

        # Test if update_highscore calls histogram's update_highscore method with the player
        self.highscore.update_highscore(mock_player)
        self.mock_histogram.update_highscore.assert_called_once_with(mock_player)

    def test_histogram_property(self):
        # Test if the histogram property returns the correct histogram object
        self.assertEqual(self.highscore.histogram, self.mock_histogram)

if __name__ == '__main__':
    unittest.main()