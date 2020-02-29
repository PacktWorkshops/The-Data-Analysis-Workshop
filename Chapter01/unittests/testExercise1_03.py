import random
import unittest
from scipy.stats import ttest_1samp

from utils import prepare_data


class TestExercise1_03(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()
        self.population_mean = self.data.registered.mean()
        self.sample = self.data[(self.data.season == "summer") & (self.data.yr == 2011)].registered

    def test_average_rides(self):
        self.assertAlmostEqual(self.population_mean, 153.786, places=2)
        self.assertAlmostEqual(self.sample.mean(), 144.732, places=2)

    def test_results(self):
        test_result = ttest_1samp(self.sample, self.population_mean)

        self.assertAlmostEqual(test_result[0], -3.492, places=2)
        self.assertAlmostEqual(test_result[1], 0, places=2)
