import unittest
from services import calculate_discount, final_price

class TestServices(unittest.TestCase):
    
    # Unit tests for calculate_discount function
    def test_calculate_discount(self):
        # Normal cases
        self.assertEqual(calculate_discount(100, 10), 10)  # 10% of 100 is 10
        self.assertEqual(calculate_discount(200, 15), 30)  # 15% of 200 is 30
        self.assertEqual(calculate_discount(50, 5), 2.5)   # 5% of 50 is 2.5
        
        # Edge cases
        self.assertEqual(calculate_discount(0, 50), 0)     # Price is 0, discount should be 0
        self.assertEqual(calculate_discount(100, 0), 0)    # Discount is 0%, final discount should be 0
        
        # Invalid cases (negative values)
        with self.assertRaises(ValueError):
            calculate_discount(-100, 10)  # Negative price should raise ValueError
        
        with self.assertRaises(ValueError):
            calculate_discount(100, -10)  # Negative discount should raise ValueError
        
        # Edge case: large values
        self.assertEqual(calculate_discount(1000000, 10), 100000)  # 10% of 1,000,000 is 100,000


    # Integration tests for final_price function
    def test_final_price(self):
        # Testing integration of final_price function with calculate_discount
        self.assertEqual(final_price(100, 10), 90)  # 100 - (10% of 100) = 90
        self.assertEqual(final_price(200, 15), 170) # 200 - (15% of 200) = 170
        self.assertEqual(final_price(50, 5), 47.5)  # 50 - (5% of 50) = 47.5
        
        # Edge case: Price is 0, the final price should also be 0
        self.assertEqual(final_price(0, 50), 0)
        
        # Edge case: Price is 100, discount is 0, the final price should remain 100
        self.assertEqual(final_price(100, 0), 100)
        
        # Invalid cases: Price or discount is negative, should raise ValueError
        with self.assertRaises(ValueError):
            final_price(-100, 10)  # Invalid price
        
        with self.assertRaises(ValueError):
            final_price(100, -10)  # Invalid discount

if __name__ == '__main__':
    unittest.main()
