# SDET 101-102 - Spring 2025
# Ricardo DaSilveira
# rcd4@njit.edu
# 212-05-998



import statistics
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
scores = [88, 76, 90, 85, 92, 67, 73, 81, 95, 78, 84, 79, 91, 87, 74, 69, 80, 82, 77, 89]

#calculate statistical data on the grade scores
scoreMin = min(scores)
scoreMax = max(scores)
scoreMean = statistics.mean(scores)
scoreMedian = statistics.median(scores)
scoreMode = statistics.mode(scores)
scoreStdDev = round(statistics.stdev(scores),2)


# create a plot of 12"x6" and let matplotlib automatically adjust the spacing between them
fig = plt.figure(figsize=(12,6),constrained_layout=True)
#create create with column aspect ratio of 3:1 
gs = fig.add_gridspec(2,2, figure = fig, width_ratios=[3, 1])

# create sub plots as grid, 
histPlot = fig.add_subplot(gs[0,0])
linePlot = fig.add_subplot(gs[1,0])
#last graph spans both rows to better accomodate analysis text
analysisPlot = fig.add_subplot(gs[0:,1])

#plot grapsh in their expect graids
histPlot.hist(scores, bins=10, edgecolor='black')
#sort the scores list in asceding order before plotting it
scores.sort()
linePlot.plot(scores)

#add graph grids
histPlot.grid(axis='y',linewidth=0.3) #smaller grid lines only on the y-axis look better
linePlot.grid()

#add Titles and and axis labels for all subplots
histPlot.set_title("Distribution of Scores")
histPlot.set_xlabel("Score")
histPlot.set_ylabel("Frequency")
linePlot.set_title("Sorted Scores")
linePlot.set_xlabel("Index")
linePlot.set_ylabel("Score")
analysisPlot.set_title("Result Analysis")
#remove the axis from the text analysis graph since we wont need it
analysisPlot.axis('off')
analysis_text = (
    
f"- The minimum score is {scoreMin}.\n"
f"- The maximum score is {scoreMax}.\n"
f"- The average score is {scoreMean}.\n"
f"- The median score is {scoreMedian}.\n"
f"- The mode of the scores is {scoreMode}.\n"
f"- The standard deviation of the scores is {scoreStdDev}.\n"
    "\n"
    "The histogram shows that most students scored between 70 and 90, with a few outliers on either end. "
    "The sorted scores graph further illustrates this trend, showing a gradual increase in scores. "
    "The standard deviation suggests that while there is some variability in the scores, it is not extreme. "
    "Overall, the scores indicate a generally good performance with no major anomalies.\n"
)
#add the analysis text to the graph
analysisPlot.text(0,0.99,analysis_text, ha='left', va='top', wrap=True)

plt.show()