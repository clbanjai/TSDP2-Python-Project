import pandas as pd
import matplotlib.pyplot as plt
import os

# report=pd.read_csv("C:\Users\claud\OneDrive - Massachusetts Institute of Technology\GTL\TSDP2\Custom-Report-2024-12-01-Estructura de generación (MW).csv")
# print(report.head)

directory_path = os.path.dirname(__file__)
file_list = os.listdir(directory_path)
old_file = "Custom-Report-2024-12-01-Estructura de generación (MW).csv"

# energy_data = pd.read_csv("2024-12-10.csv")


# print(file[14:24])
# files=os.listdir(directory_path)

# for filename in files:
#     if "Custom-Report" in filename:
#         os.rename(filename,f"{filename[14:24]}.csv")
import pandas as pd

# Specify the file path
file_path = "2024-12-01.csv"

# List of the correct column names
column_names = [
    "Hora", "Eólica", "Nuclear", "Fuel/gas", "Carbón",
    "Ciclo combinado", "Hidráulica", "Intercambios int",
    "Enlace balear", "Solar fotovoltaica", "Solar térmica",
    "Térmica renovable", "Cogeneración y residuos"
]

# Read the CSV file, skipping the first few rows with unwanted data
# report = pd.read_csv(file_path)

# print(report.head())

# Drop the extra 'Unnamed' column (if exists)
# report = report.loc[:, ~report.columns.str.contains('^Unnamed')]

# Manually set the correct column names
# report.columns = column_names

# Display the cleaned data with the correct column names
files = os.listdir(directory_path)
df_list=[]
for file in files:
    if "2024" in file:


        data_frame=pd.read_csv(file,encoding='ISO-8859-1', skiprows= 3)



        data_frame = data_frame.loc[:, ~data_frame.columns.str.contains('^Unnamed')]
        data_frame.columns = column_names
        df_list.append(data_frame)

total_data = pd.concat(df_list)

# print(total_data.iloc[:40])

total_data["Hora"] = pd.to_datetime(total_data["Hora"])

print(total_data.shape)
total_data.set_index("Hora", inplace=True)
print(total_data.shape)


hourly_data = total_data.resample('H').sum()


# hourly_data = hourly_data.loc["2024-12-01 00:00:00"::]
# print(hourly_data.head(-1))

# print(hourly_data.head())
# Convert 'Hora' column to datetime
# df['Hora'] = pd.to_datetime(df['Hora'])

# Set 'Hora' as the index
# df.set_index('Hora', inplace=True)

# Resample to hourly frequency, summing the values within each hour
# df_hourly = df.resample('H').sum()
