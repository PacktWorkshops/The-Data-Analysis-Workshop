import unittest

import numpy as np

from utils import prepare_data


class TestExercise3_01(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()
        self.numerical_features = [col for col in self.data.columns if np.issubdtype(self.data[col].dtype, np.number)]

    def test_means(self):
        target_means = [40.024, 258.285, 2.567, 962.475, 0.172]
        for col, trg_mean in zip(self.numerical_features[:5], target_means):
            self.assertAlmostEqual(self.data[col].mean(), trg_mean, places=2)
