import unittest
from scipy.stats import pearsonr, kstest, yeojohnson

from utils import prepare_data


class TestActivity2_01(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_ks(self):
        ks_res = kstest(self.data["Service time"], "norm")

        self.assertAlmostEqual(ks_res[0], 0.989, places=2)
        self.assertAlmostEqual(ks_res[1], 0., places=2)

    def test_transformed_corr(self):
        service_time = self.data["Service time"]
        absenteeism_time = yeojohnson(self.data["Absenteeism time in hours"].apply(float))[0]

        pearson_corr = pearsonr(service_time, absenteeism_time)
        self.assertAlmostEqual(pearson_corr[0], -0.042, places=2)
        self.assertAlmostEqual(pearson_corr[1], 0.25, places=2)

    def test_sons(self):
        means = self.data[["Son", "Service time"]].groupby("Son").mean()

        self.assertAlmostEqual(means["Service time"][0], 13.238, places=2)
        self.assertAlmostEqual(means["Service time"][1], 10.899, places=2)
        self.assertAlmostEqual(means["Service time"][2], 14.147, places=2)
        self.assertAlmostEqual(means["Service time"][3], 12, places=2)
        self.assertAlmostEqual(means["Service time"][4], 11, places=2)
