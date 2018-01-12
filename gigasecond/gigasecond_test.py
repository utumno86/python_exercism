<<<<<<< HEAD
import unittest

from datetime import datetime
=======
from datetime import datetime
import unittest
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd

from gigasecond import add_gigasecond


<<<<<<< HEAD
# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class GigasecondTest(unittest.TestCase):
    def test_date_only_specification_of_time(self):
        self.assertEqual(
            add_gigasecond(datetime(2011, 4, 25)),
            datetime(2043, 1, 1, 1, 46, 40))

    def test_another_date_only_specification_of_time(self):
        self.assertEqual(
            add_gigasecond(datetime(1977, 6, 13)),
            datetime(2009, 2, 19, 1, 46, 40))

    def test_one_more_date_only_specification_of_time(self):
        self.assertEqual(
            add_gigasecond(datetime(1959, 7, 19)),
            datetime(1991, 3, 27, 1, 46, 40))

    def test_full_time_specified(self):
        self.assertEqual(
            add_gigasecond(datetime(2015, 1, 24, 22, 0, 0)),
            datetime(2046, 10, 2, 23, 46, 40))

    def test_full_time_with_day_roll_over(self):
        self.assertEqual(
            add_gigasecond(datetime(2015, 1, 24, 23, 59, 59)),
            datetime(2046, 10, 3, 1, 46, 39))
=======
class GigasecondTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            datetime(2043, 1, 1, 1, 46, 40),
            add_gigasecond(datetime(2011, 4, 25))
        )

    def test_2(self):
        self.assertEqual(
            datetime(2009, 2, 19, 1, 46, 40),
            add_gigasecond(datetime(1977, 6, 13))
        )

    def test_3(self):
        self.assertEqual(
            datetime(1991, 3, 27, 1, 46, 40),
            add_gigasecond(datetime(1959, 7, 19))
        )

    def test_4(self):
        self.assertEqual(
            datetime(2046, 10, 2, 23, 46, 40),
            add_gigasecond(datetime(2015, 1, 24, 22, 0, 0))
        )

    def test_5(self):
        self.assertEqual(
            datetime(2046, 10, 3, 1, 46, 39),
            add_gigasecond(datetime(2015, 1, 24, 23, 59, 59))
        )
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd

    def test_yourself(self):
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = datetime(1970, 1, 1)
        your_gigasecond = datetime(2001, 9, 9, 1, 46, 40)

<<<<<<< HEAD
        self.assertEqual(add_gigasecond(your_birthday), your_gigasecond)

=======
        self.assertEqual(
            your_gigasecond,
            add_gigasecond(your_birthday)
        )
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd

if __name__ == '__main__':
    unittest.main()
