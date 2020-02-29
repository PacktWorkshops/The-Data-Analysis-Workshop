import unittest

from scipy.stats import ks_2samp

from utils import prepare_data


class TestExercise3_03(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_ks_age(self):
        yes_mask = self.data["y"] == "yes"
        values_yes = self.data["age"][yes_mask]
        values_no = self.data["age"][~yes_mask]

        kstest_res = ks_2samp(values_yes, values_no)

        self.assertAlmostEqual(kstest_res[0], 0.086, places=2)
        self.assertAlmostEqual(kstest_res[1], 0, places=2)

    def test_ks_duration(self):
        yes_mask = self.data["y"] == "yes"
        values_yes = self.data["duration"][yes_mask]
        values_no = self.data["duration"][~yes_mask]

        kstest_res = ks_2samp(values_yes, values_no)

        self.assertAlmostEqual(kstest_res[0], 0.464, places=2)
        self.assertAlmostEqual(kstest_res[1], 0, places=2)

    def test_ks_euribor3m(self):
        yes_mask = self.data["y"] == "yes"
        values_yes = self.data["euribor3m"][yes_mask]
        values_no = self.data["euribor3m"][~yes_mask]

        kstest_res = ks_2samp(values_yes, values_no)

        self.assertAlmostEqual(kstest_res[0], 0.432, places=2)
        self.assertAlmostEqual(kstest_res[1], 0, places=2)
