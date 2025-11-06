"""
Test file for main.py currency converter with user-friendly error messages
"""
import unittest
from main import usd_to_inr


class TestUsdToInr(unittest.TestCase):
    """Test cases for USD to INR conversion function"""
    
    def test_valid_integer(self):
        """Test conversion with valid integer input"""
        self.assertEqual(usd_to_inr(5), 415.5)
        
    def test_valid_float(self):
        """Test conversion with valid float input"""
        self.assertEqual(usd_to_inr(10.5), 872.55)
        
    def test_zero(self):
        """Test conversion with zero"""
        self.assertEqual(usd_to_inr(0), 0.0)
        
    def test_none_input(self):
        """Test that None input raises user-friendly ValueError"""
        with self.assertRaises(ValueError) as context:
            usd_to_inr(None)
        self.assertIn("USD amount cannot be None", str(context.exception))
        
    def test_string_input(self):
        """Test that string input raises user-friendly ValueError"""
        with self.assertRaises(ValueError) as context:
            usd_to_inr("abc")
        self.assertIn("Invalid input type", str(context.exception))
        self.assertIn("str", str(context.exception))
        
    def test_negative_input(self):
        """Test that negative input raises user-friendly ValueError"""
        with self.assertRaises(ValueError) as context:
            usd_to_inr(-5)
        self.assertIn("cannot be negative", str(context.exception))
        
    def test_list_input(self):
        """Test that list input raises user-friendly ValueError"""
        with self.assertRaises(ValueError) as context:
            usd_to_inr([1, 2, 3])
        self.assertIn("Invalid input type", str(context.exception))
        self.assertIn("list", str(context.exception))


if __name__ == "__main__":
    unittest.main()
