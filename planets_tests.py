import unittest
from planets import *

# Write more test cases!

class Test_planets(unittest.TestCase):

    def test_mars(self) -> None:
        weight = 136
        self.assertAlmostEqual(weight_on_planets(weight,"Mars"),51.68)

    def test_jupiter(self) -> None:
        weight = 150
        self.assertAlmostEqual(weight_on_planets(weight, "Jupiter"), 351.0)

    def test_venus(self) -> None:
        weight = 100
        self.assertAlmostEqual(weight_on_planets(weight, "Venus"), 91.0)

    def test_error(self) -> None:
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            weight = 99
            weight_on_planets(weight,"Neptune")

if __name__ == "__main__":
        unittest.main()
