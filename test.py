"""
Test module for the pi calculation function.
"""

import unittest
from decimal import Decimal
from main import calculate_pi, arctan


class TestPiCalculation(unittest.TestCase):
    """Test cases for pi calculation function."""
    
    def test_pi_five_decimal_places(self):
        """Test that pi is calculated correctly to 5 decimal places."""
        pi_value = calculate_pi(5)
        expected = Decimal("3.14159")
        self.assertEqual(pi_value, expected)
    
    def test_pi_is_decimal(self):
        """Test that the return type is Decimal."""
        pi_value = calculate_pi(5)
        self.assertIsInstance(pi_value, Decimal)
    
    def test_pi_ten_decimal_places(self):
        """Test pi calculation to 10 decimal places."""
        pi_value = calculate_pi(10)
        expected = Decimal("3.1415926536")
        self.assertEqual(pi_value, expected)
    
    def test_pi_two_decimal_places(self):
        """Test pi calculation to 2 decimal places."""
        pi_value = calculate_pi(2)
        expected = Decimal("3.14")
        self.assertEqual(pi_value, expected)
    
    def test_pi_one_decimal_place(self):
        """Test pi calculation to 1 decimal place."""
        pi_value = calculate_pi(1)
        expected = Decimal("3.1")
        self.assertEqual(pi_value, expected)
    
    def test_pi_zero_decimal_places(self):
        """Test pi calculation to 0 decimal places (integer)."""
        pi_value = calculate_pi(0)
        expected = Decimal("3")
        self.assertEqual(pi_value, expected)
    
    def test_arctan_basic(self):
        """Test that arctan returns a reasonable value."""
        result = arctan(Decimal(1) / Decimal(5))
        # arctan(1/5) should be approximately 0.197395... (in radians)
        self.assertGreater(result, Decimal("0.19"))
        self.assertLess(result, Decimal("0.20"))
    
    def test_pi_value_within_range(self):
        """Test that pi value is within expected range."""
        pi_value = calculate_pi(5)
        # Pi should be between 3.14 and 3.15
        self.assertGreater(pi_value, Decimal("3.14"))
        self.assertLess(pi_value, Decimal("3.15"))
    
    def test_multiple_calculations_consistent(self):
        """Test that multiple calls return the same value."""
        pi1 = calculate_pi(5)
        pi2 = calculate_pi(5)
        self.assertEqual(pi1, pi2)


if __name__ == "__main__":
    # Run all tests with verbose output
    unittest.main(verbosity=2)
