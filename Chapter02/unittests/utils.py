import pandas as pd


def prepare_data():
    data = pd.read_csv(
        'https://raw.githubusercontent.com/PacktWorkshops/Introduction-to-Data-Analysis/master/Chapter02/data/Absenteeism_at_work.csv',
        sep=";")

    # define encoding dictionaries
    month_encoding = {1: "January", 2: "February", 3: "March", 4: "April",
                      5: "May", 6: "June", 7: "July", 8: "August",
                      9: "September", 10: "October", 11: "November", 12: "December", 0: "Unknown"}
    dow_encoding = {2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}
    season_encoding = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    education_encoding = {1: "high_school", 2: "graduate", 3: "postgraduate", 4: "master_phd"}
    yes_no_encoding = {0: "No", 1: "Yes"}

    # backtransform numerical variables to categorical
    data["Month of absence"] = data["Month of absence"] \
        .apply(lambda x: month_encoding[x])
    data["Day of the week"] = data["Day of the week"] \
        .apply(lambda x: dow_encoding[x])
    data["Seasons"] = data["Seasons"] \
        .apply(lambda x: season_encoding[x])
    data["Education"] = data["Education"] \
        .apply(lambda x: education_encoding[x])
    data["Disciplinary failure"] = data["Disciplinary failure"] \
        .apply(lambda x: yes_no_encoding[x])
    data["Social drinker"] = data["Social drinker"] \
        .apply(lambda x: yes_no_encoding[x])
    data["Social smoker"] = data["Social smoker"] \
        .apply(lambda x: yes_no_encoding[x])

    return data
