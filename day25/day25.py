import unittest
from scipy.special import binom

POW_BASE = 252533
MOD_BASE = 33554393
FACTOR = 20151125


def calculate_code(n):
    return (FACTOR * pow(POW_BASE, n - 1, MOD_BASE)) % MOD_BASE

def get_element_number(row_num, col_num):
    return (row_num + col_num - 2) * (row_num + col_num -1) // 2 + col_num

class MyTestCase(unittest.TestCase):
    def test_calculate_code(self):
        self.assertEqual(20151125, calculate_code(1))
        self.assertEqual(31916031, calculate_code(2))
        self.assertEqual(18749137, calculate_code(3))
        self.assertEqual(16080970, calculate_code(4))
        self.assertEqual(33511524, calculate_code(21))

    def test_get_element_number(self):
        self.assertEqual(1, get_element_number(1, 1))
        self.assertEqual(2, get_element_number(2, 1))
        self.assertEqual(3, get_element_number(1, 2))
        self.assertEqual(13, get_element_number(3, 3))
        self.assertEqual(21, get_element_number(1, 6))

    def test_part_1(self):
        print(calculate_code(get_element_number(2947, 3029)))

if __name__ == '__main__':
    unittest.main()
