import unittest
from adventofcode2021.day4.tasks.day4_tasks import day4_tasks
import numpy as np

class Test_test_day4(unittest.TestCase):

    def test_task1_number(self):
        t1 = day4_tasks('resource/dataset_test.csv')
        actual = t1.playAll().numbers[-1]
        expected = 24
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_row(self):
        t1 = day4_tasks('resource/dataset_test.csv')
        actual = t1.playAll().winnerRow()
        expected = np.array([14, 21, 17, 24, 4])
        self.assertTrue((actual==expected).all(), 'Wrong result')
        return

    def test_task1_row_sum(self):
        t1 = day4_tasks('resource/dataset_test.csv')
        actual = t1.playAll().unmarkedNumbers().sum()
        expected = 188
        self.assertTrue((actual==expected).all(), 'Wrong result')
        return


    def test_task1(self):
        t1 = day4_tasks('resource/dataset_test.csv')
        actual = t1.calc()
        expected = 188 * 24 # 4512
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_real(self):
        t1 = day4_tasks('resource/dataset.csv')
        actual = t1.calc()
        expected = 668 * 66 # 44088
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2(self):
        t1 = day4_tasks('resource/dataset_test.csv')
        actual = t1.calc_last()
        expected = 148 * 13 # = 1924
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_real(self):
        t1 = day4_tasks('resource/dataset.csv')
        actual = t1.calc_last()
        expected = 23670 # = 23670
        self.assertEqual(actual, expected, 'Wrong result')
        return


if __name__ == '__main__':
    unittest.main()
