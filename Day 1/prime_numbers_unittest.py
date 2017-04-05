import unittest
from prime_numbers_generator import prime_numbers_generator

class TestPrimeNumbersGenerator(unittest.TestCase):
    def test_flow(self):
        result = prime_numbers_generator(50)
        self.assertEqual(result, ("2,3,5,7,11,13,17,19,23,29,31,37,41,43,47"))

    def test_positive_numbers_allowed(self):
        result = prime_numbers_generator(-4)
        self.assertEqual(result, "Invalid input, only positive numbers allowed")

    def test_n_greater_than_0(self):
        result = prime_numbers_generator(0)
        self.assertEqual(result, "No prime numbers between 0 and 0")

    def test_n_is_is_an_integer(self):
        result = prime_numbers_generator("ian")
        self.assertEqual(result, "Only integers allowed")

    def test_1_is_not_prime(self):
        result = prime_numbers_generator(1)
        self.assertEqual(result, "")
        
