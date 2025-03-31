import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, MultipleLocator
from api_key import API_KEY


#function = "TIME_SERIES_DAILY_ADJUSTED"
#adjusted data is behind a paywall, free stuff is better

#define function to load the data so it can be easily reused for multiple stocks
def getStockData(ticker, apiKey, fileName):
#this function returns of tuple, error indicator a True or False
# it first tries to load data from a file,
# if it fails, it tries to download from alphavantage.com
    error = True
    try: #try to use the saved data since API provider is stingy
        with open(fileName,'r') as dataFile:
            data = json.load(dataFile)
            #print the data nicely formatted so we can check it
            print(json.dumps(data, indent=5))
            error = False
    #try to download fresh data in case the file is not there
    except Exception as e: 
        print(f"An error occurred: {e}")
        print("Will try to download fresh new data!")
        
        try:
            function = "TIME_SERIES_DAILY"
            url =(f"https://www.alphavantage.co/query?function={function}&"
            f"symbol={ticker}&apikey={API_KEY}")
            #print the url for ciriosity and get the data
            print( url)
            r = requests.get(url)
            # check for any connection errors
            r.raise_for_status() 
            #unpack the data
            data = r.json()
            #good data always contains the "Meta Data" key
            if "Meta Data" in data: 
                with open(fileName,"w") as outfile:
                    json.dump(data,outfile)
                error = False
            else:
                raise Exception(f"There was a problem with the API request: {data}")    
        except requests.exceptions.RequestException as e:
            data = f"An error occurred fetching data from the internet. {e}"
        except Exception as e:
            data = f"{e}"
    return error, data   
              

#set the ticker symbols
#ticker1 = "BA"
ticker1 = "AAPL"
dataFile1 = f"{ticker1}.json"

# ticker2 = "GOOG"
# ticker2 = "RTX"
ticker2 = "MSFT"
dataFile2 = f"{ticker2}.json"

#collect data, quit if an error is found
err, ticker1data = getStockData(ticker1, API_KEY, dataFile1)
if (err):
    print(ticker1data)
    quit()

err, ticker2data = getStockData(ticker2, API_KEY, dataFile2)
if (err):
    print(ticker2data)
    quit()

#take a pick at teh data
print(ticker1data)
print("==============================")
print(ticker2data)
print("==============================")



#create a dictonary for each ticker with only the wanted data
ticker1Parsed = {}
for k, v in ticker1data['Time Series (Daily)'].items():
    ticker1Parsed[k] = v['4. close']

ticker2Parsed = {}
for k, v in ticker2data['Time Series (Daily)'].items():
    ticker2Parsed[k] = v['4. close']

# Create a DataFrame from the parsed dictionary
df_ticker1 = pd.DataFrame({
    "Date": pd.to_datetime(list(ticker1Parsed.keys()),format='%Y-%m-%d'),
    "Price": [float(price) for price in ticker1Parsed.values()]
})
#create a new column for the daily returns and change it to percentage
df_ticker1["daily_return"] = df_ticker1.Price.pct_change()*100
print(df_ticker1)
# Create a DataFrame from the dictionary
df_ticker2 = pd.DataFrame({
    "Date": pd.to_datetime(list(ticker2Parsed.keys()),format='%Y-%m-%d'),
    "Price": [float(price) for price in ticker2Parsed.values()]
})
#create a new column for the daily returns and change it to percentage
df_ticker2["daily_return"] = df_ticker2.Price.pct_change()*100
print(df_ticker2)


#========= Plot the Data =============

#create a 16"x8" image
fig = plt.figure(figsize=(16,9),constrained_layout=True,)
#create 2rows x 3 cols subplots 
gs = fig.add_gridspec(2,3, figure = fig,width_ratios=[2, 1, 1], height_ratios=[2,1])

#create the subplots and add to the grid
linePlot = fig.add_subplot(gs[0,0])
histGram1 = fig.add_subplot(gs[0,1])
histGram2 = fig.add_subplot(gs[0,2])
#use the entire bolttom roll for the analysis space 
analysisArea = fig.add_subplot(gs[1, :])


#Give titles
linePlot.set_title("Price Fluctuation")
histGram1.set_title(f"{ticker1} Daily Returns")
histGram2.set_title(f"{ticker2} Daily Returns")
analysisArea.set_title("Stock Performance Comparison")


#Label the axis
linePlot.set_xlabel("Date")
linePlot.set_ylabel("Price ($)")
histGram1.set_xlabel("Variation(%)")
histGram1.set_ylabel("Frequency")
histGram2.set_xlabel("Variation(%)")
#histGram2.set_ylabel("Frequency")

#set grids
linePlot.grid(True)
#smaller grid lines only on the y-axis look better
histGram1.grid(axis='y',linewidth=0.3) 
histGram2.grid(axis='y',linewidth=0.3) 

#add the line graphs
linePlot.plot(df_ticker1.Date,df_ticker1.Price, label=f"{ticker1}")
linePlot.plot(df_ticker2.Date,df_ticker2.Price, label=f"{ticker2}")

#add data labels to the line plot graph
linePlot.legend()

# Create ticker1 histogram with 20 bins.
counts, bins, patches = histGram1.hist(df_ticker1.daily_return, bins=20, alpha=0.75, edgecolor='black')
# Calculate the center of each bin for placing the labels
bin_centers = 0.5 * (bins[:-1] + bins[1:])
# Add labels to each bin showinbg the number of occurrences
for count, x in zip(counts, bin_centers):
    histGram1.text(x, count, f'{int(count)}', ha='center', va='bottom')
#change the number of major tick positions for a more precise analisys
histGram1.xaxis.set_major_locator(MaxNLocator(nbins=20))

#===== Repeat for ticker 2 histogram ==========
# Create ticker2 histogram with 20 bins.
counts, bins, patches = histGram2.hist(df_ticker2.daily_return, bins=20, alpha=0.75, edgecolor='black', color="tab:orange")
# Calculate the center of each bin for placing the labels
bin_centers = 0.5 * (bins[:-1] + bins[1:])
# Add labels to each bin showinbg the number of occurrences
for count, x in zip(counts, bin_centers):
    histGram2.text(x, count, f'{int(count)}', ha='center', va='bottom')
#change the number of major tick positions for a more precise analisys
histGram2.xaxis.set_major_locator(MaxNLocator(nbins=20))


#roate the x-axis tick mark labels 90 degrees
linePlot.tick_params(axis='x', which='major', labelrotation=90) 
histGram1.tick_params(axis='x', which='major', labelrotation=90) 
histGram2.tick_params(axis='x', which='major', labelrotation=90)

# Increase the number of major ticks using MaxNLocator
linePlot.xaxis.set_major_locator(MaxNLocator(nbins=50))  # up to 20 ticks

# Set minor ticks (e.g., every 0.5 units)
linePlot.xaxis.set_minor_locator(MultipleLocator(1))


#======= Analysis =============

# Calculate Mean Daily Return and Volatility
ticker1_mean_return = round(df_ticker1['daily_return'].mean(),3)
ticker2_mean_return = round(df_ticker2['daily_return'].mean(),3)

ticker1_volat = round(df_ticker1['daily_return'].std(),3)
ticker2_volat = round(df_ticker2['daily_return'].std(),3)

analysis_text=(
    #f"{ticker1}"
    f"{ticker1} shows a volatile downward trend over time, with noticeable price fluctuations. "
    "Its daily returns exhibit both sharp positive and negative spikes, indicating high variability.\n"
    f"{ticker2} also demonstrates volatility but with less severe fluctuations in its price. \n"
    f"{ticker1} histogram of daily returns shows a wider spread, suggesting more pronounced swings "
    f"while {ticker2}'s distribution appears more concentrated around zero.\n"
    f"Comparing the two, {ticker1} appears riskier with larger price swings and more extreme returns,"
    f"while {ticker2} shows relatively steadier performance with milder fluctuations.\n\n"
)

ticker1_txt = (
    f"{ticker1} mean return: {ticker1_mean_return}%\n"
    f"{ticker1} volatility: {ticker1_volat}%\n\n"
)
ticker2_txt = (
    f"{ticker2} mean return: {ticker2_mean_return}%\n"
    f"{ticker2} volatility: {ticker2_volat}%"
)

#plot the analysis text
analysisArea.text(0.2,10,analysis_text + ticker1_txt + ticker2_txt, ha='left', va='top', wrap=True)

#add axix values to facilitate placement of text
analysisArea.axis((0,9.5,0,10))


#remove axis lines for a better appearence
analysisArea.set_axis_off()

fig.suptitle(f'{ticker1} and {ticker2} Stock Price In the Last 100 Days', size=20)
plt.show()


