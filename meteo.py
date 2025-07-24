from meteostat import Point, Hourly, Daily
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

latitude=42.343992
longitude= -3.696906
start_time = dt.datetime(2024, 12, 25)
end_time = dt.datetime(2025, 1, 8)
point=Point(latitude,longitude)
new_data=Hourly(point,start_time,end_time).fetch()
new_data = new_data.rename(columns={
        'temp': 'temperature',
        'rhum': 'humidity',
        'prcp': 'precipitation',
        'wspd': 'windspeed',
        'coco': 'cloudcover'
    })

temperature_current=new_data['temperature'].to_numpy()
time=list(new_data.index)
# print(new_data)
start_time = dt.datetime(2023, 7, 1)
end_time = dt.datetime(2025, 1, 5)
new_data=Hourly(point,start_time,end_time).fetch()
new_data = new_data.rename(columns={
        'temp': 'temperature',
        'rhum': 'humidity',
        'prcp': 'precipitation',
        'wspd': 'windspeed',
        'coco': 'cloudcover'
    })

clean_data=new_data.dropna(axis=1)
clean_data.to_csv("weather_data.csv")
