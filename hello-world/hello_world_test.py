import unittest

import hello_world


<<<<<<< HEAD
# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0
=======
# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd

class HelloWorldTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world.hello(), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
