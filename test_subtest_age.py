import unittest

from age import categorize_by_age


class TestIsChild(unittest.TestCase):
    def test_child_ages(self):
        for age in range(0, 10):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")


class TestIsAdult(unittest.TestCase):
    def test_adult_ages(self):
        for age in range(19, 66):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")


class TestIsGoldenAge(unittest.TestCase):
    def test_golden_age_ages(self):
        for age in range(66, 151):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Golden age")


if __name__ == "__main__":
    unittest.main(verbosity=2)
