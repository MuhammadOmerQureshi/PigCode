import unittest
from intelligence import (
    Intelligence,
)  # Adjust this import based on your actual file structure


class TestIntelligence(unittest.TestCase):
    def test_turn_score_at_threshold(self):
        """Test turn score exactly at the threshold"""
        intelligence = Intelligence(20)
        self.assertTrue(
            intelligence.decide_hold(20),
            "Should return True when turn score equals the threshold.",
        )

    def test_turn_score_above_threshold(self):
        """Test turn score above the threshold"""
        intelligence = Intelligence(20)
        self.assertTrue(
            intelligence.decide_hold(25),
            "Should return True when turn score is above the threshold.",
        )

    def test_turn_score_below_threshold(self):
        """Test turn score below the threshold"""
        intelligence = Intelligence(20)
        self.assertFalse(
            intelligence.decide_hold(15),
            "Should return False when turn score is below the threshold.",
        )

    def test_change_threshold(self):
        """Test functionality after changing the threshold"""
        intelligence = Intelligence(20)
        intelligence.threshold = 30
        self.assertFalse(
            intelligence.decide_hold(25),
            "Should return False when turn score is below the new threshold.",
        )
        self.assertTrue(
            intelligence.decide_hold(30),
            "Should return True when turn score equals the new threshold.",
        )
        self.assertTrue(
            intelligence.decide_hold(35),
            "Should return True when turn score is above the new threshold.",
        )

    def test_negative_turn_score(self):
        """Test with a negative turn score"""
        intelligence = Intelligence(20)
        self.assertFalse(
            intelligence.decide_hold(-5),
            "Should return False when turn score is negative.",
        )


if __name__ == "__main__":
    unittest.main()
