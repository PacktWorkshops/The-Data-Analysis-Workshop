import unittest
import pandas as pd
from statsmodels.tsa.stattools import adfuller

from utils import prepare_data


class TestExercise1_06(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

        self.daily_rides = self.data[["dteday", "registered", "casual"]]
        self.daily_rides = self.daily_rides.groupby("dteday").sum()
        self.daily_rides.index = pd.to_datetime(self.daily_rides.index)

    def stationarity(self, ts, window=10):
        data = pd.DataFrame(ts)
        data['rolling_mean'] = ts.rolling(window).mean()
        data['rolling_std'] = ts.rolling(window).std()

        return adfuller(ts)

    def test_stationarity(self):
        daily_rides = self.data[["dteday", "registered", "casual"]]
        daily_rides = daily_rides.groupby("dteday").sum()

        registered_res = self.stationarity(daily_rides["registered"])
        casual_res = self.stationarity(daily_rides["casual"])

        self.assertAlmostEqual(registered_res[0], -1.851, places=2)
        self.assertAlmostEqual(registered_res[1], 0.355, places=2)
        self.assertAlmostEqual(casual_res[0], -1.817, places=2)
        self.assertAlmostEqual(casual_res[1], 0.371, places=2)

    def test_ma(self):
        registered_ma = self.data["registered"].rolling(10).mean()
        registered_ma_diff = self.data["registered"] - registered_ma
        registered_ma_diff.dropna(inplace=True)

        casual_ma = self.data["casual"].rolling(10).mean()
        casual_ma_diff = self.data["casual"] - casual_ma
        casual_ma_diff.dropna(inplace=True)

        registered_res = self.stationarity(registered_ma_diff)
        casual_res = self.stationarity(casual_ma_diff)

        self.assertAlmostEqual(registered_res[0], -27.859, places=2)
        self.assertAlmostEqual(registered_res[1], 0, places=2)
        self.assertAlmostEqual(casual_res[0], -24.836, places=2)
        self.assertAlmostEqual(casual_res[1], 0, places=2)
