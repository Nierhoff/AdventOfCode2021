import unittest
from adventofcode2021.day9.tasks.day9_tasks import day9_tasks
import numpy as np

class Test_test_day6(unittest.TestCase):

    def test_task1_low_map(self):
        t1 = day9_tasks('resource/dataset_test.csv')
        actual = t1.get_low_map().sum()
        expected = 4
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_risk(self):
        t1 = day9_tasks('resource/dataset_test.csv')
        actual = t1.get_risk_map().sum()
        expected = 15
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_risk_real(self):
        t1 = day9_tasks('resource/dataset.csv')
        actual = t1.get_risk_map().sum()
        expected = 539
        self.assertEqual(actual, expected, 'Wrong result')
        return

if __name__ == '__main__':
    unittest.main()
