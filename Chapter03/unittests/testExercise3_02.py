import unittest

from utils import prepare_data


class TestExercise3_02(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_counts_marital(self):
        counts = self.data["marital"].value_counts()

        self.assertEqual(counts["married"], 24928)
        self.assertEqual(counts["single"], 11568)
        self.assertEqual(counts["divorced"], 4612)
        self.assertEqual(counts["unknown"], 80)

    def test_counts_housing(self):
        counts = self.data["housing"].value_counts()

        self.assertEqual(counts["yes"], 21576)
        self.assertEqual(counts["no"], 18622)
        self.assertEqual(counts["unknown"], 990)

    def test_counts_day_of_week(self):
        counts = self.data["day_of_week"].value_counts()

        self.assertEqual(counts["thu"], 8623)
        self.assertEqual(counts["mon"], 8514)
        self.assertEqual(counts["wed"], 8134)
        self.assertEqual(counts["tue"], 8090)
        self.assertEqual(counts["fri"], 7827)
