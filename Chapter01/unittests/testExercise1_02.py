import unittest

from utils import prepare_data


class TestExercise1_02(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_time_series(self):
        plot_data = self.data[['registered', 'casual', 'dteday']]
        plot_data = plot_data.groupby('dteday').sum()

        self.assertEqual(plot_data.head(1).values.tolist()[0], [654, 331])
        self.assertEqual(plot_data.tail(1).values.tolist()[0], [2290, 439])

    def test_rolling_time_series(self):
        plot_data = self.data[['registered', 'casual', 'dteday']]
        plot_data = plot_data.groupby('dteday').sum()

        window = 7
        rolling_means = plot_data.rolling(window).mean().values[-1].tolist()
        rolling_deviations = plot_data.rolling(window).std().values[-1].tolist()

        self.assertAlmostEqual(rolling_means[0], 1461, places=1)
        self.assertAlmostEqual(rolling_means[1], 328.85, places=1)
        self.assertAlmostEqual(rolling_deviations[0], 791.43, places=1)
        self.assertAlmostEqual(rolling_deviations[1], 209.32, places=1)

    def test_melt_weekday(self):
        plot_data = self.data[['hr', 'weekday', 'registered', 'casual']]
        plot_data = plot_data.melt(id_vars=['hr', 'weekday'], var_name='type', value_name='count')

        head = plot_data.head(1).values[0]
        tail = plot_data.tail(1).values[0]

        self.assertEqual(head.tolist(), [0, "Saturday", "registered", 13])
        self.assertEqual(tail.tolist(), [23, "Monday", "casual", 12])

    def test_melt_season(self):
        plot_data = self.data[['hr', 'season', 'registered', 'casual']]
        plot_data = plot_data.melt(id_vars=['hr', 'season'], var_name='type', value_name='count')

        head = plot_data.head(1).values[0]
        tail = plot_data.tail(1).values[0]

        self.assertEqual(head.tolist(), [0, "winter", "registered", 13])
        self.assertEqual(tail.tolist(), [23, "winter", "casual", 12])

    def test_melt_hr(self):
        plot_data = self.data[['hr', 'season', 'registered', 'casual']]
        plot_data = plot_data.melt(id_vars=['hr', 'season'], var_name='type', value_name='count')

        head = plot_data.head(1).values[0]
        tail = plot_data.tail(1).values[0]

        self.assertEqual(head.tolist(), [0, "winter", "registered", 13])
        self.assertEqual(tail.tolist(), [23, "winter", "casual", 12])

    def test_melt_season(self):
        plot_data = self.data[['weekday', 'season', 'registered', 'casual']]
        plot_data = plot_data.melt(id_vars=['weekday', 'season'], var_name='type', value_name='count')

        head = plot_data.head(1).values[0]
        tail = plot_data.tail(1).values[0]

        self.assertEqual(head.tolist(), ["Saturday", "winter", "registered", 13])
        self.assertEqual(tail.tolist(), ["Monday", "winter", "casual", 12])
