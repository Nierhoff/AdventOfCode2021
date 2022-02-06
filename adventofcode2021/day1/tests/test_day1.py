import unittest
from adventofcode2021.day1.tasks.day1_tasks import day1_tasks

class Test_test_task1(unittest.TestCase):
    def test_task1(self):
        t1 = day1_tasks('resource/dataset_test.csv')
        actual = t1.calc()
        expected = 7
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_real(self):
        t1 = day1_tasks('resource/dataset.csv')
        actual = t1.calc()
        expected = 1791
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2(self):
        t2 = day1_tasks('resource/dataset_test.csv')
        actual = t2.calc_movingAverage()
        expected = 5
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_real(self):
        t2 = day1_tasks('resource/dataset.csv')
        actual = t2.calc_movingAverage()
        expected = 1822
        self.assertEqual(actual, expected, 'Wrong result')
        return


if __name__ == '__main__':
    unittest.main()
