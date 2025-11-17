# https://github.com/CrazyMoosen/lab10-AB-JP
# Partner 1: Advay Bhangale
# Partner 2: Jainish Patel

import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
    ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(10, 50), 500)
        self.assertEqual(mul(0, 100), 0)
        self.assertAlmostEqual(mul(3.14, 2.0), 6.28)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(1, 2), 0.5)
        self.assertAlmostEqual(div(1, 5), 0.2)
        self.assertAlmostEqual(div(1, 8), 0.125)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(math.e, math.e**2), 2)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(-1, 50)
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(-3.0, 4.0), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(20, 21), 29, places=5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-10)

        with self.assertRaises(ValueError):
            square_root(-510)

        with self.assertRaises(ValueError):
            square_root(-854.45434)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()