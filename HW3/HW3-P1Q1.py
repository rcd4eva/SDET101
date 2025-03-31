import statistics
import matplotlib.pyplot as plt
import numpy as np # using numpy for easy quartile calculations on Question 3


#==============================================================================
# Part 1: Histogram Analysis
#==============================================================================
orange_weights = [150, 152, 149, 155, 148, 151, 153, 154, 152, 150,
                  149, 151, 152, 153, 154, 155, 156, 157, 158, 159,
                  160, 158, 157, 156, 155, 154, 153, 152, 151, 150,
                  149, 148, 147, 146, 145, 146, 147, 148, 149, 150,
                  151, 152, 153, 154, 155, 156, 157, 158, 159, 160]


mean = statistics.mean(orange_weights)
median = statistics.median(orange_weights)
mode = statistics.mode(orange_weights)
std_deviation = statistics.stdev(orange_weights)

# Creating the figure with two plot areas
fig, ax = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [3, 1]})

#plot area 1
ax[0].hist(orange_weights)
ax[0].text(145, 9, f'Mean: {mean:.2f}')
ax[0].text(145, 8.5, f'Median: {median:.2f}')
ax[0].text(145, 8, f'Mode: {mode}')
ax[0].text(145, 7.5, f'Standard Deviation: {std_deviation:.2f}')
ax[0].set_xlabel('Orange Weights')
ax[0].set_ylabel('Frequency')

analysis_text = (
    "Histogram Analysis:\n"
    "- The distribution is roughly symmetric.\n"
    "- Mean, median, and mode are closely aligned.\n"
    "- The spread indicates moderate variability.\n"
    "- Most weights cluster near the center, resembling a normal distribution."
)

#plot area 2 - histogram analysis
ax[1].axis('off')
ax[1].text(0, 0.5, analysis_text, va='center', ha='left', fontsize=12, wrap=True)
plt.tight_layout() # keep the teo subplots close to each other
plt.show()



