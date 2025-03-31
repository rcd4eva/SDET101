import matplotlib.pyplot as plt
import requests

#==============================================================================
# Part 2 - Question 4: Data Retrieval from APIs and Visualization
#==============================================================================

url="https://api.exchangerate-api.com/v4/latest/USD"
data = requests.get(url).json() 

euro = (data['rates']['EUR'])
dollar = (data['rates']['USD'])
jyen = (data['rates']['JPY'])
gbp = (data['rates']['GBP'])


currencies = ['EUR', 'GBP', 'JPY']
exchange_rates = [euro, gbp,jyen]

fig, ax = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [3, 1]})

#plot area 1
ax[0].bar(currencies, exchange_rates, color=['blue', 'green', 'red'])
ax[0].set_title('Exchange Rates Relative to USD')
ax[0].set_xlabel('Currency')
ax[0].set_ylabel('Exchange Rate')
ax[0].text(0, 140, f'1 USD = {euro:.2f} Euros', ha='left', va='bottom')
ax[0].text(0, 130 , f'1 USD = {gbp:.2f} British Pound', ha='left', va='bottom')
ax[0].text(0, 120 , f'1 USD = {jyen:.2f} Japanese Yen', ha='left', va='bottom')

#plot area 2 - analysis
analysis_text = (
    f"- Euro (EUR): With 1 USD equating to approximately {euro} EUR, the US Dollar is relatively strong against the Euro. "
    "Increasing the purchasing power of American travelers and businesses in Eurozone countries, "
    "making goods and services more affordable.\n\n"
    f" - British Pound (GBP): At 1 USD equal to about {gbp} GBP, the Dollar exhibits considerable strength against the Pound. "
    "This rate benefits Americans purchasing British products or traveling to the UK.\n\n"
    f" - Japanese Yen (JPY): The exchange rate of 1 USD to approximately {jyen} JPY indicates a robust Dollar relative to the Yen. "
    "This rate favors American consumers and companies importing Japanese goods, as they receive more value for each Dollar spent."


)

ax[1].axis('off')
ax[1].text(0, 0.5, analysis_text, va='center', ha='left', fontsize=12, wrap=True)
plt.tight_layout() # keep the teo subplots close to each other
plt.show()