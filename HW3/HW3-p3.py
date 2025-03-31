
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

#==============================================================================
# Part 3: Website Traffic Analysis
#==============================================================================

url="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"
data = requests.get(url).json() 

print(data['features'])

print(data)
#create a list for date, magnitude and places to faciliate plotting the graph
date = []
magnitude = []
places = []
for i in range(0,len(data['features'])):
    #date = datetime.date(datetime.fromtimestamp(data['features'][i]['properties']['time']))
    dateRaw = int(data['features'][i]['properties']['time'])/1000
    place = data['features'][i]['properties']['place']
    mag = data['features'][i]['properties']['mag']
    date.append (datetime.fromtimestamp(dateRaw).strftime('%Y-%m-%d %H:%M:%S'))
    magnitude.append(data['features'][i]['properties']['mag'])
    places.append(data['features'][i]['properties']['place'])
    print(f"date: {dateRaw},  magnitude: {mag}, location: {place}")


#create two subplots, one for hte graph and one for the analysis
fig, ax = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [3, 1]})


ax[0].set_title('Earthquake Magnitudes Over Time')
ax[0].set_xlabel('Time of Occurrence')
ax[0].set_ylabel('Magnitude')
ax[0].grid(True)
ax[0].scatter(date, magnitude)
#change the frequency of the x-axis major tick mark to every 20 records
ax[0].xaxis.set_major_locator(plt.MaxNLocator(nbins=20))
#rotate x-tick lavel 90 degree 
ax[0].set_xticklabels(date, rotation=90,)

#find the highest magnitude to print in the analysis
maxMag = max(magnitude)

#plot area 2 - analysis
analysis_text = (
    "Analysis:\n"
"- Earthquakes in the dataset mostly have magnitudes ranging from 4.5 to 5.2.\n"
"- The occurrences are relatively spread out over time without clear clustering.\n"
"- Frequency of occurances decreases exponentially as the maginute increases.\n"
f"- The highest recorded magnitude is during the time period was {maxMag}.\n"
"- There is an earthquake somewhere in the world every few minutes"

)

ax[1].axis('off')
ax[1].text(0, 0.5, analysis_text, va='center', ha='left', fontsize=12, wrap=True)
plt.tight_layout() # keep the teo subplots close to each other
plt.show()


