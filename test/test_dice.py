import unittest
from dice import Dice


class TestDice(unittest.TestCase):
    def test_roll(self):
        # Test if roll returns a valid value within the expected range
        roll = Dice.roll()
        self.assertTrue(1 <= roll <= 6)

    def test_roll_multiple_times(self):
        # Test if roll returns different values on multiple calls
        rolls = set()
        for _ in range(1000):
            rolls.add(Dice.roll())
        self.assertTrue(len(rolls) > 1)


if __name__ == "__main__":
    unittest.main()
