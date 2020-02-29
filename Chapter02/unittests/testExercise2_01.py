import unittest

from utils import prepare_data


class TestExercise2_01(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def in_icd(self, val):
        return "Yes" if val >= 1 and val <= 21 else "No"

    def test_dimensions(self):
        self.assertEqual(self.data.shape, (740, 21))

    def test_bars(self):
        self.data["Disease"] = self.data["Reason for absence"].apply(self.in_icd)

        values = self.data["Disease"].value_counts()

        self.assertEqual(values["No"], 478)
        self.assertEqual(values["Yes"], 262)
