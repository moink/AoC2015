import unittest
from string import ascii_lowercase
import pandas as pd

password = 'cqjxjnds'


def add_one(prev):
    nums = [ord(char) for char in reversed(prev)]
    i = 0
    done = False
    while not done:
        if nums[i] < ord('z'):
            nums[i] = nums[i] + 1
            done = True
        else:
            nums[i] = ord('a')
            i = i + 1
    result = ''.join(chr(num) for num in reversed(nums))
    return result

def check_password(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    zero_count = 0
    test_password = password
    for i in range(len(password) - 1):
        if test_password[i] == test_password[i+1] and test_password[i] != '#':
            zero_count = zero_count + 1
            test_password = test_password.replace(test_password[i], '#')
    if zero_count < 2:
        return False
    diffs = '_' + '_'.join(str(ord(password[i+1]) - ord(password[i]))
             for i in range(len(password) - 1)) + '_'
    return '_1_1_' in diffs


def get_next_password(prev):
    new_password = add_one(prev)
    while check_password(new_password) is False:
        new_password = add_one(new_password)
    return new_password


class TestPassword(unittest.TestCase):
    def test_add_one_simple(self):
        result = add_one('aaaaaaaa')
        self.assertEqual('aaaaaaab', result)

    def test_add_one_carrying(self):
        result = add_one('aaaaaaaz')
        self.assertEqual('aaaaaaba', result)

    def test_add_one_carrying_twice(self):
        result = add_one('aaaaaazz')
        self.assertEqual('aaaaabaa', result)

    def test_check_password(self):
        self.assertTrue(check_password('abcdffaa'))
        self.assertTrue(check_password('cqjxxyzz'))
        self.assertFalse(check_password('hijklmmn'))

    def test_part_1(self):
        result = get_next_password('cqjxxyzz')
        self.assertEqual('cqjxxyzz', result)

if __name__ == '__main__':
    unittest.main()
