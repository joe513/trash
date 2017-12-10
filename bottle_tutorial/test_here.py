import unittest
import here

g = 'Hello'


class MyTestCase(unittest.TestCase):

    def test_d(self):
        self.assertEqual(g.upper(), 'HELLO')



if __name__ == '__main__':
    unittest.main()
