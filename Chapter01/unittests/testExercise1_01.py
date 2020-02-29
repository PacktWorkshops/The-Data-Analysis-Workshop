import unittest

from utils import prepare_data


class TestExercise1_01(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_dimensions(self):
        self.assertEqual(self.data.shape, (17379, 17))

    def test_season(self):
        self.assertEqual(self.data["season"].unique().tolist(), ['winter', 'spring', 'summer', 'fall'])

    def test_yr(self):
        self.assertEqual(self.data["yr"].unique().tolist(), [2011, 2012])

    def test_weekday(self):
        self.assertEqual(self.data["weekday"].unique().tolist(),
                         ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

    def test_weathersit(self):
        self.assertEqual(self.data["weathersit"].unique().tolist(),
                         ['clear', 'cloudy', 'light_rain_snow', 'heavy_rain_snow'])

    def test_hum(self):
        self.assertEqual(self.data["hum"].max(), 100.0)
        self.assertEqual(self.data["hum"].min(), 0.0)

    def test_windspeed(self):
        self.assertAlmostEqual(self.data["windspeed"].max(), 56.9, delta=0.1)
        self.assertEqual(self.data["windspeed"].min(), 0.0)
