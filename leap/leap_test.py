import unittest

from leap import is_leap_year


<<<<<<< HEAD
# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class YearTest(unittest.TestCase):
    def test_year_not_divisible_by_4(self):
        self.assertIs(is_leap_year(2015), False)

    def test_year_divisible_by_4_not_divisible_by_100(self):
        self.assertIs(is_leap_year(1996), True)

    def test_year_divisible_by_100_not_divisible_by_400(self):
        self.assertIs(is_leap_year(2100), False)

    def test_year_divisible_by_400(self):
        self.assertIs(is_leap_year(2000), True)
=======
# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class YearTest(unittest.TestCase):
    def test_year_not_divisible_by_4(self):
        self.assertFalse(is_leap_year(2015))

    def test_year_divisible_by_4_not_divisible_by_100(self):
        self.assertTrue(is_leap_year(2016))

    def test_year_divisible_by_100_not_divisible_by_400(self):
        self.assertFalse(is_leap_year(2100))

    def test_year_divisible_by_400(self):
        self.assertTrue(is_leap_year(2000))
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd


if __name__ == '__main__':
    unittest.main()
