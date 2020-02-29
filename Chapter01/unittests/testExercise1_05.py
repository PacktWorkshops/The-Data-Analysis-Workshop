import unittest
import numpy as np
from scipy.stats import spearmanr

from utils import prepare_data


class TestExercise1_05(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_pearson(self):
        cols = ["temp", "atemp", "hum", "windspeed"]
        registered_correlations = [0.335, 0.332, -0.273, 0.082]
        casual_correlations = [0.459, 0.454, -0.347, 0.090]

        for col, corr in zip(cols, registered_correlations):
            self.assertAlmostEqual(np.corrcoef(self.data[col], self.data.registered)[0, 1], corr, places=2)

        for col, corr in zip(cols, casual_correlations):
            self.assertAlmostEqual(np.corrcoef(self.data[col], self.data.casual)[0, 1], corr, places=2)

    def test_spearman(self):
        cols = ["temp", "atemp", "hum", "windspeed"]
        registered_correlations = [0.373, 0.373, -0.338, 0.122]
        casual_correlations = [0.57, 0.57, -0.388, 0.122]

        for col, corr in zip(cols, registered_correlations):
            self.assertAlmostEqual(spearmanr(self.data[col], self.data["registered"])[0], corr, places=2)

        for col, corr in zip(cols, casual_correlations):
            self.assertAlmostEqual(spearmanr(self.data[col], self.data["casual"])[0], corr, places=2)
