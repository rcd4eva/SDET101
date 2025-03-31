import pandas as pd
import matplotlib.pyplot as plt

#check for errors when opening the file
try:
    df = pd.read_csv("./monthly_sales.csv")
except Exception as e:
    print(e)
    quit()
else:
    print(df.Sales)

#check to see if the list slice contains the correct data
print(df.Month.str[:3])

#create a 16"x8" image
fig = plt.figure(figsize=(16,8),constrained_layout=True,)
#create 2rows x 3 cols subplot grid spaces
gs = fig.add_gridspec(2,3, figure = fig)

#add the subplots to each grid
#and share the y-axis between all the graphs on the 1st row
barChart = fig.add_subplot(gs[0,0])
linePlot = fig.add_subplot(gs[0,1], sharey=barChart)
qtrBarPlot = fig.add_subplot(gs[0,2],sharey=barChart)
analysisNbrs = fig.add_subplot(gs[1,:]) # 2nd row, 1st column
#analysisTxt = fig.add_subplot(gs[1,-1]) # 2nd row, 2nd column

#add titles
barChart.set_title("Bar Chart Monthly Sales")
linePlot.set_title("Line Plot Monthly Sales")
qtrBarPlot.set_title("Quaterly Results")
analysisNbrs.set_title("Sales Analysis", loc='left',fontsize=20, pad=10)

#set y-axis label (only the first graph since they are shared)
barChart.set_ylabel("Sales (US$)")

#turn off y_tick lables for the line and quaterly graphs
plt.setp(linePlot.get_yticklabels(), visible=False)
plt.setp(qtrBarPlot.get_yticklabels(), visible=False)

#set grids
barChart.grid(True)
linePlot.grid(True)
qtrBarPlot.grid(True)

#remove the x-axis grid for a cleaner look
barChart.xaxis.set_visible(False)
qtrBarPlot.xaxis.set_visible(False)

#completely remove both axis from Analysis since it is only text
analysisNbrs.set_axis_off()
colrs = ['tab:blue']*3 + ['tab:orange']*3 + ['tab:green']*3 + ['tab:red']*3
print(colrs)

#plot monthly bar graph
barObj = barChart.bar(df.Month, df.Sales, label = df.Month, color=colrs)
#add the Month's first 3 characters to the top of the bar
barChart.bar_label(barObj, df.Month.str[:3])


#plot the line graph
#set x-axis tick labels to the month's first 3 letters and rotate 90 degrees
linePlot.set_xticklabels(df.Month.str[:3],rotation = 90)
#add the monthly sales values to the line markers
j = 0
for x,y in zip(df.Month,df.Sales):
    linePlot.plot(df.Month[j:j+2],df.Sales[j:j+2], marker='D', color = colrs[j])
    linePlot.text(x,y+300,f"${y}",ha='center', va='bottom')
    
    j +=1
#plot the quaterly sale bar graph
#use the same for loop to generate the quaterly numbers, create the bars,
# and add labels to the top of the bar
for i in range(0,4):
    x = i*3
    #use list slicing to devide the sales into quaters
    q = round(df[x:x+3].Sales.mean())
    #plot the bar graph for the quater
    qtrBarPlot.bar(f"Q{i+1}",q)
    #add the quater value in dollar to the of the bar
    qtrBarPlot.text(i,q, f"${q}",ha='center', va='bottom')
    #just checking
    print(f"q{i+1}")
    print(df[x:x+3])

#finally, generate the analysis data and message
total_sales = df.Sales.sum()
avg_month_sales = round(df.Sales.mean())
best_sales_moth = df.Sales.max()
worst_sales_month = df.Sales.min()

print(f"Total Sales: {total_sales}")
print(f"Average Monthly Sales: {avg_month_sales}")
print(f"Best month: {best_sales_moth}")
print(f"Worst Month:{worst_sales_month}")

analysis_nbrs = (
    #f"Temperature Analysis:\n"
    f"Total Sales: ${total_sales}\n"
    f"Average Monthly Sales: ${avg_month_sales}\n"
    f"Best month: ${best_sales_moth}\n"
    f"Worst Month: ${worst_sales_month}\n\n"

    f"The monthly sales show an upward trend, starting at ${worst_sales_month} in January"
    f" and peaking at {best_sales_moth} in December,"
    "with minor fluctuations in between.\n"
    "Quaterly numbers clearly show strong growth through the year.\n"
    "A good marketing campaing was most likely the cause in order to maintain such strong numbers outside shopping holidays season"
    
)
#add axix values to facilitate placement of text
analysisNbrs.axis((0,10,0,10))
analysisNbrs.text(0.01,9.5,analysis_nbrs,fontsize=12, wrap=True, va="top", ha="left")





fig.suptitle('Monthly Sales', size=20)
plt.show()