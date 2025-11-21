"""
Test suite for main.py currency conversion module.
"""
import unittest
import time
from main import usd_to_inr, validate_amount, USD_TO_INR_RATE


class TestValidateAmount(unittest.TestCase):
    """Tests for the validate_amount function."""
    
    def test_valid_positive_int(self):
        """Test with valid positive integer."""
        result = validate_amount(10)
        self.assertEqual(result, 10.0)
        self.assertIsInstance(result, float)
    
    def test_valid_positive_float(self):
        """Test with valid positive float."""
        result = validate_amount(10.5)
        self.assertEqual(result, 10.5)
    
    def test_valid_zero(self):
        """Test with zero value."""
        result = validate_amount(0)
        self.assertEqual(result, 0.0)
    
    def test_none_raises_error(self):
        """Test that None raises ValueError."""
        with self.assertRaises(ValueError) as context:
            validate_amount(None)
        self.assertIn("cannot be None", str(context.exception))
    
    def test_negative_raises_error(self):
        """Test that negative values raise ValueError."""
        with self.assertRaises(ValueError) as context:
            validate_amount(-5)
        self.assertIn("cannot be negative", str(context.exception))
    
    def test_string_raises_error(self):
        """Test that non-numeric strings raise TypeError."""
        with self.assertRaises(TypeError) as context:
            validate_amount("invalid")
        self.assertIn("must be numeric", str(context.exception))
    
    def test_numeric_string_accepted(self):
        """Test that numeric strings are converted properly."""
        result = validate_amount("10.5")
        self.assertEqual(result, 10.5)


class TestUsdToInr(unittest.TestCase):
    """Tests for the usd_to_inr conversion function."""
    
    def test_basic_conversion(self):
        """Test basic USD to INR conversion."""
        result = usd_to_inr(5)
        expected = 5 * USD_TO_INR_RATE
        self.assertEqual(result, expected)
    
    def test_zero_conversion(self):
        """Test conversion of zero."""
        result = usd_to_inr(0)
        self.assertEqual(result, 0.0)
    
    def test_large_amount(self):
        """Test conversion of large amounts."""
        result = usd_to_inr(10000)
        expected = 10000 * USD_TO_INR_RATE
        self.assertEqual(result, expected)
    
    def test_decimal_amount(self):
        """Test conversion of decimal amounts."""
        result = usd_to_inr(1.5)
        expected = 1.5 * USD_TO_INR_RATE
        self.assertAlmostEqual(result, expected, places=2)
    
    def test_negative_raises_error(self):
        """Test that negative amounts raise error."""
        with self.assertRaises(ValueError):
            usd_to_inr(-10)
    
    def test_none_raises_error(self):
        """Test that None raises error."""
        with self.assertRaises(ValueError):
            usd_to_inr(None)
    
    def test_caching_performance(self):
        """Test that caching improves performance for repeated calls."""
        # Clear cache to start fresh
        usd_to_inr.cache_clear()
        
        # First call - will compute
        start = time.perf_counter()
        result1 = usd_to_inr(100)
        first_call_time = time.perf_counter() - start
        
        # Second call with same input - should be cached
        start = time.perf_counter()
        result2 = usd_to_inr(100)
        second_call_time = time.perf_counter() - start
        
        # Results should be identical
        self.assertEqual(result1, result2)
        
        # Cached call should be faster or at least not significantly slower
        # We don't assert it's faster because the function is so simple
        # that the difference might not be measurable, but we verify
        # the cache is working by checking cache_info
        cache_info = usd_to_inr.cache_info()
        self.assertEqual(cache_info.hits, 1)  # One cache hit
        self.assertEqual(cache_info.misses, 1)  # One cache miss
    
    def test_cache_multiple_values(self):
        """Test that cache handles multiple different values."""
        usd_to_inr.cache_clear()
        
        # Call with different values
        usd_to_inr(10)
        usd_to_inr(20)
        usd_to_inr(10)  # This should be a cache hit
        usd_to_inr(20)  # This should be a cache hit
        
        cache_info = usd_to_inr.cache_info()
        self.assertEqual(cache_info.hits, 2)
        self.assertEqual(cache_info.misses, 2)


if __name__ == "__main__":
    unittest.main()
