import unittest

from scipy.stats import ttest_ind

from utils import prepare_data


class TestExercise1_06(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_means(self):
        dows = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        target_means = [9.248, 7.981, 7.147, 4.424, 5.125]
        target_std = [15.973, 18.027, 13.268, 4.266, 7.911]
        for dow, trg_mean, trg_std in zip(dows, target_means, target_std):
            mask = self.data["Day of the week"] == dow
            hours = self.data["Absenteeism time in hours"][mask]
            mean = hours.mean()
            stddev = hours.std()

            self.assertAlmostEqual(mean, trg_mean, places=2)
            self.assertAlmostEqual(stddev, trg_std, places=2)

    def test_average_duration(self):
        thursday_mask = self.data["Day of the week"] == "Thursday"
        july_mask = self.data["Month of absence"] == "July"

        thursday_data = self.data["Absenteeism time in hours"] \
            [thursday_mask]
        no_thursday_data = self.data["Absenteeism time in hours"] \
            [~thursday_mask]
        july_data = self.data["Absenteeism time in hours"][july_mask]
        no_july_data = self.data["Absenteeism time in hours"][~july_mask]

        thursday_res = ttest_ind(thursday_data, no_thursday_data)
        july_res = ttest_ind(july_data, no_july_data)

        self.assertAlmostEqual(thursday_res[0], -2.307, places=2)
        self.assertAlmostEqual(thursday_res[1], 0.021, places=2)
        self.assertAlmostEqual(july_res[0], 2.605, places=2)
        self.assertAlmostEqual(july_res[1], 0.009, places=2)
