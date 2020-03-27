import unittest

import numpy as np
import pandas as pd
import statsmodels.api as sm

from utils import prepare_data


class TestExercise3_04(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_lr(self):
        X = self.data.drop("y", axis=1)
        X = pd.get_dummies(X)
        X = sm.add_constant(X)
        y = np.where(self.data["y"] == "yes", 1, 0)

        full_logistic_regression_model = sm.Logit(y, X)
        result = full_logistic_regression_model.fit(maxiter=500)

        params = result.params
        self.assertTrue(params["const"] < 0)
        self.assertAlmostEqual(params["age"], 0, places=2)
        self.assertAlmostEqual(params["duration"], 0, places=2)
