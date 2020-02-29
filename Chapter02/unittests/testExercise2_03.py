import unittest

from utils import prepare_data


class TestExercise2_03(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_means_drinkers(self):
        means = self.data[["Social drinker", "Absenteeism time in hours"]].groupby("Social drinker").mean()

        self.assertAlmostEqual(means["Absenteeism time in hours"]["Yes"], 7.68, places=2)
        self.assertAlmostEqual(means["Absenteeism time in hours"]["No"], 5.931, places=2)

    def test_means_smokers(self):
        means = self.data[["Social smoker", "Absenteeism time in hours"]].groupby("Social smoker").mean()

        self.assertAlmostEqual(means["Absenteeism time in hours"]["Yes"], 6.5, places=2)
        self.assertAlmostEqual(means["Absenteeism time in hours"]["No"], 6.957, places=2)
