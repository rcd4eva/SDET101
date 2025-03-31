# SDET 101-102 - Spring 2025
# Ricardo DaSilveira
# rcd4@njit.edu
# 212-05-998

import random
import statistics
import matplotlib.pyplot as plt


steps = [random.randint(4000, 15000) for _ in range(30)]

#generate statisticakl data
total_steps = sum(steps)
days_month = 30
avg_steps = statistics.mean(steps)
max_steps = max(steps)
min_steps = min(steps)

threshold = 10000
# high_steps = [number for number in steps if number > threshold]
high_steps = []
mod_steps = []
weekend_steps = []
weekday_steps =[]
days_goal_met = 0

#count how many days steps were above the threshold
for i,val in enumerate(steps):
    if val >=threshold:
        high_steps.append(val)
        mod_steps.append(val)
        days_goal_met += 1 
    else:
        high_steps.append(float('nan'))
        mod_steps.append(val)
    #find the weekend and weekday values
    if i%7 < 5:
        weekday_steps.append(val)
    else:
        weekend_steps.append(val)
        
#take a peek at the parsed data
print(weekday_steps)
print(weekend_steps)

#illustration oh how the weekends steps are found
# i, mod, weekday
# 0,  0,  monday
# 1,  1,  tue
# 2,  2,  wed
# 3,  3,  thu
# 4,  4,  fri
# 5,  5,  sat <=
# 6,  6,  sun <=
# 7,  0,  mon
# 8,  1,  tue
# 9,  2,  wed
# 10, 3,  thu
# 11, 4,  fri
# 12, 5,  sat <=
# 13, 6,  sun <=
# 14, 0,  mon 

avg_weekend_steps = statistics.mean(weekend_steps)
avg_weekday_steps = statistics.mean(weekday_steps)

print(avg_weekday_steps)
print(avg_weekend_steps)
#plot the data
fig = plt.figure(figsize=(12,6),constrained_layout=True)

#create a figure 1 row and 2 columns with aspect ratio of 3:1 
gs = fig.add_gridspec(1,2, figure = fig, width_ratios=[2, 1])

# create sub plots as grid, 
linePlot = fig.add_subplot(gs[0,0])
analysisPlot = fig.add_subplot(gs[0,1])

#add titles and labels
linePlot.set_title("Steps over 30 days")
linePlot.set_xlabel("Days")
linePlot.set_ylabel("Steps")
analysisPlot.set_title("Analysis")
analysisPlot.axis('off')

#plot the graphs
linePlot.plot(mod_steps)
linePlot.plot(high_steps, color='red', marker='o')
linePlot.axhline(y=threshold, color="r", linewidth=0.5, label=f"{threshold} Steps")
linePlot.legend()

#=================analysis===============

# Calculate the percentage of days the 10,000-step goal was met
percentage_goal_met = (days_goal_met / days_month) * 100

# Compare average steps on weekdays versus weekends
weekdays_steps = [steps[i] for i in range(days_month) if i % 7 < 5]
weekends_steps = [steps[i] for i in range(days_month) if i % 7 >= 5]

avg_weekdays_steps = statistics.mean(weekdays_steps)
avg_weekends_steps = statistics.mean(weekends_steps)

# # Display the analysis
if avg_weekend_steps >  avg_weekday_steps:
    steps_comparison_txt = ["higher","It must have been a nice weekend!"]

elif avg_weekend_steps < avg_weekday_steps:
    steps_comparison_txt = ["lower","Work, work, work, work, work, work!\n "]
else:
    steps_comparison_txt = ["equal","Work balance life!\n "]
analysis_text = (
    f"Total Steps: {total_steps}\n"
    f"Average Steps: {avg_steps:.2f}\n"
    f"Max Steps: {max_steps}\n"
    f"Min Steps: {min_steps}\n"
    f"Number of Days Above {threshold} Steps: {days_goal_met} ({percentage_goal_met:.1f}%)\n"
    f"Average Weekday Steps: {avg_weekday_steps:.0f}\n"
    f"Average Weekend Steps: {avg_weekend_steps:.0f}\n\n"
    f"Weekend average step count was {steps_comparison_txt[0]} than in the weekdays. \n\n"
    f"{steps_comparison_txt[1]}"
)

analysisPlot.text(0.1, 0.95, analysis_text, fontsize=12, ha='left', va='top', wrap=True)

plt.show()