import unittest
from adventofcode2021.day8.tasks.day8_tasks import day8_tasks
import numpy as np

class Test_test_day6(unittest.TestCase):

    def test_task1_shorts(self):
        t1 = day8_tasks('resource/dataset_test.csv')
        actual = t1.calc()
        expected = 26
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_shorts_real(self):
        t1 = day8_tasks('resource/dataset.csv')
        actual = t1.calc()
        expected = 479
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_solve(self):
        t1 = day8_tasks('resource/dataset_test.csv')
        actual = t1.solve()
        expected = True
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_solve_real(self):
        t1 = day8_tasks('resource/dataset.csv')
        actual = t1.solve()
        expected = True
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_calc_output(self):
        t1 = day8_tasks('resource/dataset_test.csv')
        actual = t1.calc_output_value()
        expected = 61229
        self.assertEqual(actual, expected, 'Wrong result')
        return

if __name__ == '__main__':
    unittest.main()
