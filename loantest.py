import unittest
from Bootcamp import loan_calculator

class loanCalculator(unittest.TestCase):
    def test_month(self):
        result = loan_calculator(10000, 12, 15)
        self.assertEqual(result, "Invalid input")

        result = loan_calculator(1000, 12, -1)
        self.assertEqual(result, "Invalid input")
