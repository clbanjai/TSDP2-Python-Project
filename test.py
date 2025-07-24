from meteostat import Point, Hourly
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

start_time = datetime.datetime(2024, 12, 25)
end_time = datetime.datetime(2025,1,13)
latitude = 42.3555
longitude = 71.0565
#Boston Coordinates
point = Point(latitude,longitude) #meteostat will process the coordinates that we are interested in in
data = Hourly(point,start_time,end_time).fetch() #generates the data that we are intersted in
ad_latitude=42.5063
ad_longitude = 1.5218
ad_data=Hourly(Point(ad_latitude,ad_longitude),start_time,end_time).fetch()
clean_data=data.dropna(axis=1)



# small_data= clean_data.loc["2024-12-25 00:00:00","2024-12-25 03:00:00"]



# small_data.to_csv("weather_data.csv",index=True)
# print(pd.read_csv("weather_data.csv",index_col=0))



christmas_day = clean_data.loc["2024-12-25 00:00:00":"2024-12-26 00:00:00"]



december = clean_data.loc["2024-12"]





time = clean_data.index
ad_temperature = ad_data['temp']
temperature = clean_data['temp']

plt.plot(time,temperature, label = "Boston",color = 'olive')
plt.plot(time,ad_temperature, label = "Andorra",color = "yellow")
plt.legend()
plt.xlabel('Time')
plt.ylabel("Temperature °C")
plt.title("Temperature in Boston vs Andorra")
plt.grid()
plt.tight_layout()
plt.show()


# clean_data.to_csv("clean_data.csv")


# old_data = pd.read_csv("clean_data.csv",index_col=0)




# print(old_data.head())
