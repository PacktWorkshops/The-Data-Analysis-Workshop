import pandas as pd


def prepare_data():
    data = pd.read_csv(
        "https://raw.githubusercontent.com/PacktWorkshops/The-Data-Analysis-Workshop/master/Chapter03/data/bank-additional/bank-additional-full.csv",
        sep=";")

    return data
