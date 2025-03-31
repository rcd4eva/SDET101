
import statistics
import matplotlib.pyplot as plt


#==============================================================================
# Part 2: Website Traffic Analysis
#==============================================================================


daily_visitors = [120, 135, 150, 160, 155, 140, 130, 125, 150, 165,
                  170, 160, 155, 150, 145, 140, 135, 130, 125, 120,
                  115, 110, 105, 100, 95, 100, 105, 110, 115, 120]

mean = statistics.mean(daily_visitors)
std_deviation = statistics.stdev(daily_visitors)

# Creating the figure with two plot areas
fig, ax = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [3, 1]})

#plot area 1
ax[0].plot(daily_visitors, label='Daily Visitors')
ax[0].axhline(mean, color='r', linestyle='--', label='Mean')
ax[0].set_xlabel('Days')
ax[0].set_ylabel('Visitors')
ax[0].set_title('Daily Visitors over 30 Days')
ax[0].legend()

analysis_text = (
    "Analysis:\n"
    f"- Mean visitors: {mean:.2f}\n"
    f"- Std Dev: {std_deviation:.2f}\n"
    "- Visitor count peaks around day 10, then declines.\n"
    "- Possible cause: Initial traffic boost from a campaign or promotion.\n"
    "- Gradual decline may indicate fading campaign effects."
)

#plot area 2 -  analysis
ax[1].axis('off')
ax[1].text(0, 0.5, analysis_text, va='center', ha='left', fontsize=12, wrap=True)
plt.tight_layout() # keep the teo subplots close to each other
plt.show()