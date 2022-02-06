import unittest
from adventofcode2021.day5.tasks.day5_tasks import day5_tasks
import numpy as np

class Test_test_day5(unittest.TestCase):

    def test_task1_number(self):
        t1 = day5_tasks('resource/dataset_test.csv')
        actual = t1.calc()
        expected = 5
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_real(self):
        t1 = day5_tasks('resource/dataset.csv')
        actual = t1.calc()
        expected = 4655 
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_number(self):
        t1 = day5_tasks('resource/dataset_test.csv')
        actual = t1.calc_complex()
        expected = 12
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_real(self):
        t1 = day5_tasks('resource/dataset.csv')
        actual = t1.calc_complex()
        expected = 20500 
        self.assertEqual(actual, expected, 'Wrong result')
        return

if __name__ == '__main__':
    unittest.main()
