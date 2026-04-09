import unittest
from main import usd_to_inr


class TestUsdToInr(unittest.TestCase):
    RATE = 83.1

    def test_positive_integer(self):
        self.assertAlmostEqual(usd_to_inr(1), 83.1)

    def test_example_from_code(self):
        self.assertAlmostEqual(usd_to_inr(5), 415.5)

    def test_zero(self):
        self.assertAlmostEqual(usd_to_inr(0), 0.0)

    def test_negative_value(self):
        self.assertAlmostEqual(usd_to_inr(-1), -83.1)

    def test_decimal_input(self):
        self.assertAlmostEqual(usd_to_inr(0.5), 41.55)

    def test_large_value(self):
        self.assertAlmostEqual(usd_to_inr(1000), 83100.0)

    def test_fractional_cent(self):
        self.assertAlmostEqual(usd_to_inr(0.01), 0.831)

    def test_result_is_float(self):
        result = usd_to_inr(2)
        self.assertIsInstance(result, float)

    def test_conversion_rate(self):
        self.assertAlmostEqual(usd_to_inr(1), self.RATE)

    def test_linearity(self):
        self.assertAlmostEqual(usd_to_inr(3), usd_to_inr(1) + usd_to_inr(2))


if __name__ == "__main__":
    unittest.main()
