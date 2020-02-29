import random
import unittest
from scipy.stats import ttest_ind

from utils import prepare_data


class TestExercise1_04(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()
        self.population_mean = self.data.registered.mean()
        self.sample = self.data[(self.data.season == "summer") & (self.data.yr == 2011)].registered

        weekend_days = ['Saturday', 'Sunday']
        self.weekend_mask = self.data.weekday.isin(weekend_days)
        self.workingdays_mask = ~self.data.weekday.isin(weekend_days)

    def test_registered(self):
        weekend_data = self.data.registered[self.weekend_mask]
        workingdays_data = self.data.registered[self.workingdays_mask]

        test_res = ttest_ind(weekend_data, workingdays_data)
        self.assertAlmostEqual(test_res[0], -16.004, places=2)
        self.assertAlmostEqual(test_res[1], 0, places=2)

    def test_casual(self):
        weekend_data = self.data.casual[self.weekend_mask]
        workingdays_data = self.data.casual[self.workingdays_mask]

        test_res = ttest_ind(weekend_data, workingdays_data)

        self.assertAlmostEqual(test_res[0], 41.077, places=2)
        self.assertAlmostEqual(test_res[1], 0, places=2)
