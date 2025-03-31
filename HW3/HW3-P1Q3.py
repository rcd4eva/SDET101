
import matplotlib.pyplot as plt
import numpy as np # using numpy for easy quartile calculations on Question 3

#==============================================================================
# Part 3: Website Traffic Analysis
#==============================================================================

test_scores = [65, 70, 75, 80, 85, 90, 95, 85, 75, 65,
               70, 80, 90, 85, 75, 65, 70, 80, 90, 95,
               85, 75, 65, 70, 80]

min = np.min(test_scores)
q1 = np.percentile(test_scores, 25)
median = np.median(test_scores)
q3 = np.percentile(test_scores, 75)
max = np.max(test_scores)

# Creating the figure with two plot areas
fig, ax = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [3, 1]})

#plot area 1
ax[0].boxplot(test_scores, vert=False) # vert=false makes the boxplot horizontal
ax[0].set_title('Box Plot of Science Test Scores')
ax[0].set_xlabel('Scores')
ax[0].grid(axis='x', linestyle='--') #add x-axis gridlines as dashed lines

analysis_text = (
    "Five-Number Summary:\n"
    f"- Minimum: {min}\n"
    f"- Q1 (25th percentile): {q1}\n"
    f"- Median: {median}\n"
    f"- Q3 (75th percentile): {q3}\n"
    f"- Maximum: {max}\n\n"
    "Analysis:\n"
    "- Data appears roughly symmetric with a well-centered median.\n"
    "- No obvious extreme outliers are present.\n"
    "- Scores seem to cluster around the 70-90 range, indicating moderate spread."
)


#plot area 2 -  analysis
ax[1].axis('off')
ax[1].text(0, 0.5, analysis_text, va='center', ha='left', fontsize=12, wrap=True)
plt.tight_layout() # keep the teo subplots close to each other
plt.show()