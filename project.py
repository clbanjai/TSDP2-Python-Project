import requests
import json

url="https://apidatos.ree.es/es/datos/balance/balance-electrico?start_date=2019-01-01T00:00&end_date=2019-01-31T23:59&time_trunc=hour"
# &geo_limit=ccaa&geo_ids=9"
url="https://apidatos.ree.es/es/datos/generacion/estructura-generacion?start_date=2014-01-01T00:00&end_date=2018-12-31T23:59&time_trunc=hour&geo_trunc=electric_system&geo_limit=ccaa&geo_ids=7"
response=requests.get(url)
print(response.status_code)
# data=response.json()
# print(json.dumps(data,indent=4))
import json
import pandas as pd
import matplotlib.pyplot as plt


# # Extract 'included' data
# included_data = data['included']

# # Process data for renewable and non-renewable sources
# sources = []
# for group in included_data:
#     group_type = group['type']
#     for item in group['attributes']['content']:
#         attributes = item['attributes']
#         sources.append({
#             'Category': group_type,
#             'Type': attributes['title'],
#             'Total Generation (MWh)': attributes['total'],
#             'Percentage': attributes['values'][0]['percentage'],
#             'Last Update': attributes['last-update']
#         })

# # Convert to a DataFrame for easy analysis
# # print(sources)
# df = pd.DataFrame(sources)
# print(df)
# Summarize renewable and non-renewable totals
# summary = df.groupby('Category')['Total Generation (MWh)'].sum().reset_index()

# Visualization
# plt.figure(figsize=(10, 6))
# plt.pie(summary['Total Generation (MWh)'], labels=summary['Category'], autopct='%1.1f%%', startangle=140)
# plt.title("Renewable vs Non-Renewable Energy Generation")
# plt.show()

# Save to CSV
# df.to_csv("energy_data.csv", index=False)
