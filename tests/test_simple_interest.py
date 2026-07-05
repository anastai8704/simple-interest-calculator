import unittest

from simple_interest_calculator import calculate_simple_interest


class SimpleInterestCalculatorTests(unittest.TestCase):
    def test_calculates_simple_interest_correctly(self):
        self.assertEqual(calculate_simple_interest(1000, 5, 2), 100.0)

    def test_returns_zero_for_zero_values(self):
        self.assertEqual(calculate_simple_interest(0, 10, 3), 0.0)


if __name__ == "__main__":
    unittest.main()
