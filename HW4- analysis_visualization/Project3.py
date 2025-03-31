import requests
import json
import random
import statistics
import matplotlib.pyplot as plt


threshold = 10

dates = [f'Day {i+1}' for i in range(14)]
# temperatures = [random.uniform(15, 30) for _ in range(14)]  # Temperatures in °C
temperatures = [round(random.uniform(15, 30),1) for _ in range(14)]  # Temperatures in °C


#identifying anomalies
# Anomaly will be defined as a sudden change in temperature bigger then 
# a given threshold

fig = plt.figure(figsize=(12,6),constrained_layout=True)

#create a figure 1 row and 2 columns and change aspect ratio  
gs = fig.add_gridspec(1,2, figure = fig, width_ratios=[2, 1])

#add the line plot
linePlot = fig.add_subplot(gs[0,0])
linePlot.set_title("Temperature Over The Last 14 Days")
linePlot.set_xlabel("Days")
linePlot.set_ylabel("Temperature (C)")
linePlot.plot(dates,temperatures, marker='o')


anomalie_days =[]
for i in range(1, len(temperatures)):
    change = round(abs(temperatures[i] - temperatures[i-1]),1)
    if change >= threshold:
        # Highlight the segment from day i-1 to day i in red
        #using list slicing days[1:3] = days[1] to days[2], last element is excluded
        linePlot.plot(dates[i-1:i+1], temperatures[i-1:i+1], color='red')
        anomalie_days.append({'day':i,'temp':temperatures[i], 'change':change})  

print(anomalie_days)

#add the temperature to ech line marker
for i, temp in enumerate(temperatures):
    #move the data point marker annotaion 0.5 points upwards (y-axis) and 0.05 to the right (x-axis)
    linePlot.text(i+0.05, temp +0.5, f"{temp}C",ha='left', va='top', )
#change the x-ticks lables to "Day x" and rotate 90 degrees
linePlot.set_xticklabels(dates,rotation = 90)
linePlot.grid()

#===============analysis==================
analysisPlot = fig.add_subplot(gs[0,1])
analysisPlot.set_title("Temperature Analysis")
analysisPlot.set_axis_off()
min_temp = min(temperatures)
max_temp = max(temperatures)
avg_temp = statistics.mean(temperatures)
std_dev = statistics.stdev(temperatures)

analysis_text = (
    f"Min Temperature: {min_temp}°C\n"
    f"Max Temperature: {max_temp}°C\n"
    f"Average Temperature: {avg_temp:.2f}°C\n"
    f"Average Temperature Deviation: {std_dev:.2f}°C\n\n"
    
)

#print a different message dependiong on the analysis result
anomalies = len(anomalie_days)
if anomalies > 0:
    analysis_text += f"There was/were {anomalies} day(s) where the temperature changed more than {threshold}°C):\n"
    for anomaly in anomalie_days:
        analysis_text += (
            f"Day {anomaly['day']}, Change: {anomaly['change']}°C \n"    )
else:
    analysis_text += "There were no temperature anomalies observed"

    

print(analysis_text)
analysisPlot.text(0, 0.98, analysis_text, fontsize=12, ha='left', va='top', wrap=True)
plt.show()


