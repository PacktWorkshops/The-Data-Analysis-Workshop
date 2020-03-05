import pandas as pd


def prepare_data():
    data = pd.read_csv(
        "https://raw.githubusercontent.com/PacktWorkshops/Introduction-to-Data-Analysis/master/chapter03/data/bank-additional/bank-additional-full.csv",
        sep=";")

    return data
