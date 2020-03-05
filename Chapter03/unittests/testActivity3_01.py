import unittest

import numpy as np
import statsmodels.api as sm

from utils import prepare_data


class TestActivity3_01(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_model(self):
        columns = ["duration", "campaign", "pdays", "cons.price.idx",
                   "cons.conf.idx", "euribor3m"]
        X = self.data[columns]
        X = sm.add_constant(X)
        y = np.where(self.data["y"] == "yes", 1, 0)

        logistic_regression_model = sm.Logit(y, X)
        result = logistic_regression_model.fit()
        params = result.params

        self.assertAlmostEqual(params["const"], -43.137, places=2)
        self.assertAlmostEqual(params["duration"], 0.004, places=2)
        self.assertAlmostEqual(params["campaign"], -0.049, places=2)
        self.assertAlmostEqual(params["pdays"], -0.001, places=2)
        self.assertAlmostEqual(params["cons.price.idx"], 0.492, places=2)
        self.assertAlmostEqual(params["cons.conf.idx"], 0.069, places=2)
        self.assertAlmostEqual(params["euribor3m"], -0.72, places=2)
