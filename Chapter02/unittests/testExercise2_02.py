import unittest

from utils import prepare_data


class TestExercise2_02(unittest.TestCase):
    def setUp(self):
        self.data = prepare_data()

    def test_drinkers(self):
        values = self.data["Social drinker"].value_counts(normalize=True)
        self.assertAlmostEqual(values["Yes"], 0.567, places=2)
        self.assertAlmostEqual(values["No"], 0.432, places=2)

    def test_drinkers(self):
        values = self.data["Social smoker"].value_counts(normalize=True)
        self.assertAlmostEqual(values["Yes"], 0.072, places=2)
        self.assertAlmostEqual(values["No"], 0.927, places=2)

    def test_conditional_probability_example(self):
        event_a = set(["BB"])
        event_b = set(["BB", "BG", "GB"])

        cond_prob = (0.25 * len(event_a.intersection(event_b))) / (0.25 * len(event_b))
        self.assertAlmostEqual(cond_prob, 0.333, places=2)

    def test_conditional_probability(self):
        # compute probabilities of being a drinker and smoker
        drinker_prob = self.data["Social drinker"].value_counts(normalize=True)["Yes"]
        smoker_prob = self.data["Social smoker"].value_counts(normalize=True)["Yes"]

        # create mask for social drinkers/smokers
        drinker_mask = self.data["Social drinker"] == "Yes"
        smoker_mask = self.data["Social smoker"] == "Yes"

        # compute probabilities of absence reasons and being a social drinker/smoker
        total_entries = self.data.shape[0]
        absence_drinker_prob = self.data["Reason for absence"][drinker_mask].value_counts() / total_entries
        absence_smoker_prob = self.data["Reason for absence"][smoker_mask].value_counts() / total_entries

        self.assertAlmostEqual((absence_drinker_prob / drinker_prob)[0], 0.069, places=2)
        self.assertAlmostEqual((absence_smoker_prob / smoker_prob)[0], 0.148, places=2)
        self.assertAlmostEqual((absence_drinker_prob / drinker_prob)[28], 0.207, places=2)
        self.assertAlmostEqual((absence_smoker_prob / smoker_prob)[28], 0.074, places=2)
