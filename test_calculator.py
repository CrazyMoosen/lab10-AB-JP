# https://github.com/CrazyMoosen/lab10-AB-JP
# Partner 1: Advay Bhangale
# Partner 2: Jainish Patel

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(10, 50), 500)
        self.assertEqual(mul(0, 100), 0)
        self.assertAlmostEqual(mul(3.14, 2.0), 6.28)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(2, 1), 0.5)
        self.assertAlmostEqual(div(5, 1), 0.2)
        self.assertAlmostEqual(div(8, 1), 0.125)
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(-1, 50)
    ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(-3.0, 4.0), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(20, 21), 29)

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