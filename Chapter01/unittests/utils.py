import pandas as pd


def prepare_data():
    data = pd.read_csv(
        'https://raw.githubusercontent.com/PacktWorkshops/Introduction-to-Data-Analysis/master/Chapter01/data/hour.csv')

    # tranform seasons
    seasons_mapping = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'fall'}
    data['season'] = data['season'].apply(lambda x: seasons_mapping[x])

    # transform yr
    yr_mapping = {0: 2011, 1: 2012}
    data['yr'] = data['yr'].apply(lambda x: yr_mapping[x])

    # transform weekday
    weekday_mapping = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday',
                       6: 'Saturday'}
    data['weekday'] = data['weekday'].apply(lambda x: weekday_mapping[x])

    # transform weathersit
    weather_mapping = {1: 'clear', 2: 'cloudy', 3: 'light_rain_snow', 4: 'heavy_rain_snow'}
    data['weathersit'] = data['weathersit'].apply(lambda x: weather_mapping[x])

    # transorm hum and windspeed
    data['hum'] = data['hum'] * 100
    data['windspeed'] = data['windspeed'] * 67

    return data
