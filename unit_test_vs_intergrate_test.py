import unittest
from services import calculate_discount, final_price

class TestDiscountCalculations(unittest.TestCase):
    # Unit Tests
    def test_calculate_discount(self):
        """Unit test for calculate_discount function"""
        # Test regular cases
        self.assertEqual(calculate_discount(100, 10), 10)  # 10% of 100 is 10
        self.assertEqual(calculate_discount(200, 15), 30)  # 15% of 200 is 30
        
        # Test edge cases
        self.assertEqual(calculate_discount(0, 50), 0)     # Zero price
        self.assertEqual(calculate_discount(100, 0), 0)    # Zero discount
        
        # Test with floating point numbers
        self.assertAlmostEqual(calculate_discount(99.99, 10), 9.999)
        self.assertAlmostEqual(calculate_discount(199.99, 15), 29.9985)

    def test_calculate_discount_negative_values(self):
        """Unit test for handling negative values"""
        # we test it for completeness
        self.assertEqual(calculate_discount(-100, 10), -10)
        self.assertEqual(calculate_discount(100, -10), -10)

    # Integration Tests
    def test_final_price_integration(self):
        """Integration test for final_price function"""
        # Test regular cases
        self.assertEqual(final_price(100, 10), 90)    # 100 - (10% of 100)
        self.assertEqual(final_price(200, 15), 170)   # 200 - (15% of 200)
        
        # Test edge cases
        self.assertEqual(final_price(0, 50), 0)       # Zero price
        self.assertEqual(final_price(100, 0), 100)    # Zero discount
        
        # Test with floating point numbers
        self.assertAlmostEqual(final_price(99.99, 10), 89.991)
        self.assertAlmostEqual(final_price(199.99, 15), 169.9915)

    def test_final_price_full_discount(self):
        """Integration test for 100% discount"""
        self.assertEqual(final_price(100, 100), 0)    # 100% discount should result in zero
        self.assertEqual(final_price(200, 100), 0)    # 100% discount should result in zero

if __name__ == '__main__':
    unittest.main()