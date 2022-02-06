import unittest
from adventofcode2021.day6.tasks.day6_tasks import day6_tasks
import numpy as np

class Test_test_day6(unittest.TestCase):

    def test_task1_18(self):
        t1 = day6_tasks('resource/dataset_test.csv')
        actual = t1.calc_18()
        expected = 26
        self.assertEqual(actual, expected, 'Wrong result')
        return
    def test_task1_80(self):
        t1 = day6_tasks('resource/dataset_test.csv')
        actual = t1.calc_80()
        expected = 5934
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_80_real(self):
        t1 = day6_tasks('resource/dataset.csv')
        actual = t1.calc_80()
        expected = 346063
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_256(self):
        t1 = day6_tasks('resource/dataset_test.csv')
        actual = t1.calc_256()
        expected = 26984457539
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_256_real(self):
        t1 = day6_tasks('resource/dataset.csv')
        actual = t1.calc_256()
        expected = 1572358335990
        self.assertEqual(actual, expected, 'Wrong result')
        return

if __name__ == '__main__':
    unittest.main()
