import unittest

class Test_test(unittest.TestCase):

    def test(self):
        actual = 0
        expected = 0
        self.assertEqual(actual, expected, 'Wrong result')
        return

if __name__ == '__main__':
    unittest.main()
