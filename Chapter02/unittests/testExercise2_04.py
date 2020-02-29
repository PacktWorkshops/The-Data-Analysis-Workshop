import unittest
from scipy.stats import ttest_ind, pearsonr, ks_2samp

from utils import prepare_data


class TestExercise2_04(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()
        self.data["Disease"] = self.data["Reason for absence"].apply(self.in_icd)

    def in_icd(self, val):
        return "Yes" if val >= 1 and val <= 21 else "No"

    def test_pearson(self):
        pearson_test = pearsonr(self.data["Age"], self.data["Absenteeism time in hours"])

        self.assertAlmostEqual(pearson_test[0], 0.065, places=2)
        self.assertAlmostEqual(pearson_test[1], 0.073, places=2)

    def test_means(self):
        means = self.data[["Disease", "Age"]].groupby("Disease").mean()

        self.assertAlmostEqual(means["Age"]["Yes"], 36.652, places=2)
        self.assertAlmostEqual(means["Age"]["No"], 36.338, places=2)

    def test_ks(self):
        disease_mask = self.data["Disease"] == "Yes"
        disease_ages = self.data["Age"][disease_mask]
        no_disease_ages = self.data["Age"][~disease_mask]

        test_res = ttest_ind(disease_ages, no_disease_ages)
        ks_res = ks_2samp(disease_ages, no_disease_ages)

        self.assertAlmostEqual(test_res[0], 0.629, places=2)
        self.assertAlmostEqual(test_res[1], 0.529, places=2)
        self.assertAlmostEqual(ks_res[0], 0.056, places=2)
        self.assertAlmostEqual(ks_res[1], 0.618, places=2)
