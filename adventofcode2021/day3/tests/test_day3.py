import unittest
from adventofcode2021.day3.tasks.day3_tasks import day3_tasks

class Test_test_day3(unittest.TestCase):
    def test_task1_gamma(self):
        t1 = day3_tasks('resource/dataset_test.csv')
        actual = t1.get_gamma()
        expected = 22
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_epsilon(self):
        t1 = day3_tasks('resource/dataset_test.csv')
        actual = t1.get_epsilon()
        expected = 9
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1(self):
        t1 = day3_tasks('resource/dataset_test.csv')
        actual = t1.calc()
        expected = 9*22
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_oxygen (self):
        t1 = day3_tasks('resource/dataset_test.csv')
        actual = t1.get_oxygen()
        expected = 23
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_co2(self):
        t1 = day3_tasks('resource/dataset_test.csv')
        actual = t1.get_co2()
        expected = 10
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2(self):
        t1 = day3_tasks('resource/dataset_test.csv')
        actual = t1.calc_complex()
        expected = 230
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task1_real(self):
        t1 = day3_tasks('resource/dataset.csv')
        actual = t1.calc()
        expected = 1307354
        self.assertEqual(actual, expected, 'Wrong result')
        return

    def test_task2_real(self):
        t1 = day3_tasks('resource/dataset.csv')
        actual = t1.calc_complex()
        expected = 482500
        self.assertEqual(actual, expected, 'Wrong result')
        return


if __name__ == '__main__':
    unittest.main()
