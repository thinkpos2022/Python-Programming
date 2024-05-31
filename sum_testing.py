def sum_positive(numbers):
    return sum(n for n in numbers if n > 0)

def sum_negative(numbers):
    return sum(n for n in numbers if n < 0)
import unittest

class TestSumNegative(unittest.TestCase):

    # Existing tests
    def test_sum_negative_positive_numbers(self):
        numbers = [1, -14, 13, 4, -15]
        self.assertEqual(sum_negative(numbers), -29)

    def test_sum_negative_negative_numbers(self):
        numbers = [-11, -5, -3, -14, -8]
        self.assertEqual(sum_negative(numbers), -41)

    def test_sum_negative_mixed_numbers(self):
        numbers = [1, -14, 13, -4, -15, 0]
        self.assertEqual(sum_negative(numbers), -33)

    def test_sum_negative_single_positive(self):
        numbers = [1]
        self.assertEqual(sum_negative(numbers), 0)

    def test_sum_negative_single_negative(self):
        numbers = [-1]
        self.assertEqual(sum_negative(numbers), -1)

    # New test case
    def test_sum_negative_all_negative_numbers(self):
        numbers = [-1, -2, -3, -4, -5]
        self.assertEqual(sum_negative(numbers), -15)

    def test_sum_negative_all_negative_numbers_large(self):
        numbers = [-1000, -2000, -3000, -4000, -5000]
        self.assertEqual(sum_negative(numbers), -15000)

    def test_sum_negative_all_negative_numbers_mixed(self):
        numbers = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]
        self.assertEqual(sum_negative(numbers), -15)

    def test_sum_negative_all_negative_numbers_single(self):
        numbers = [-10]
        self.assertEqual(sum_negative(numbers), -10)

    def test_sum_negative_all_negative_numbers_empty(self):
        numbers = []
        self.assertEqual(sum_negative(numbers), 0)

if __name__ == '__main__':
    unittest.main()

