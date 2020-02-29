import unittest

from utils import prepare_data


class TestExercise2_05(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()
        self.education_types = ["high_school", "graduate", "postgraduate", "master_phd"]

    def test_education_counts(self):
        counts = self.data["Education"].value_counts()
        percentages = self.data["Education"].value_counts(normalize=True)

        target_counts = [611, 46, 79, 4]
        target_percentages = [82.567, 6.216, 10.675, 0.54]

        for education, trg_count in zip(self.education_types, target_counts):
            self.assertEqual(counts[education], trg_count)

        for education, trg_prc in zip(self.education_types, target_percentages):
            self.assertAlmostEqual(100 * percentages[education], trg_prc, places=2)

    def test_education_means(self):
        target_means = [7.190, 6.391, 5.266, 5.250]
        target_std = [14.259, 6.754, 7.963, 3.202]
        for educ_type, trg_mean, trg_std in zip(self.education_types, target_means, target_std):
            mask = self.data["Education"] == educ_type
            hours = self.data["Absenteeism time in hours"][mask]
            mean = hours.mean()
            stddev = hours.std()

            self.assertAlmostEqual(mean, trg_mean, places=2)
            self.assertAlmostEqual(stddev, trg_std, places=2)
