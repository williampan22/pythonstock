import datetime as dt
from fileinput import nextfile
from mimetypes import init
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import style 
import pandas as pd
import pandas_datareader
import pandas_datareader.data as web   
from pandas_datareader._utils import RemoteDataError 
import numpy as np

valid_ticker = False
valid_investment = False
valid_date = False
num_stocks = 0
extrema = [[], [], [], []]

while valid_ticker == False: 
    try: 
        str_arr = input('Enter stock tickers seperated by commas (eg. aapl, amzn): ').split(',') 
        stock_ticker = [num.strip().upper() for num in str_arr]
        
        for i in range(len(stock_ticker)): 
            broken_ticker = stock_ticker[i]
            test = web.DataReader(stock_ticker[i], 'yahoo', dt.datetime(2022, 1, 1), dt.datetime.today())
            
            
        break
    except RemoteDataError: 
        print(broken_ticker + ' was not a valid stock ticker. Try again...' )
    except KeyError: 
        print(broken_ticker + ' was not a valid stock ticker. Try again...' )

stock_ticker.append("SPY")

while valid_investment == False: 
    try: 
        initial_investment = input("Enter an inital investment in dollars (eg. 1000): ")
        test1 = float(initial_investment)

        if float(initial_investment) <= 0:
            negativeError = ValueError('Initial investment should be a positive number')
            raise negativeError
        break
    except ValueError: 
        print('That was not a valid number. Make sure your investment is positive. Try again...')
    except negativeError: 
        print('Your initial investment cannot be a negative amount of money. Try again...')

while valid_date == False: 
    try: 
        start_string = input('Enter a date in the FORMAT: {M/D/YYYY} (eg: 1/1/2022): ')
        start = dt.datetime.strptime(start_string, "%m/%d/%Y")
        break
    except ValueError: 
        print('That was not a valid date. Try again...')
    

end = dt.datetime.today()
timediff = (end-start).days


end_string = end.strftime("%m/%d/%Y")
df = web.DataReader( stock_ticker, 'yahoo', start, end)

adj_closings = df['Adj Close']



#dollar roi return for each day based on inital investment
returns = df['Adj Close']
for i in range(len(stock_ticker)): 
    start_price = returns[stock_ticker[i]].iloc[0]
    returns[stock_ticker[i]] = (returns[stock_ticker[i]] - start_price) / start_price * float(initial_investment)


daily_returns = adj_closings.pct_change()
correlation = daily_returns.corr()
print(correlation)

std = daily_returns.std()
bar_std_height = []
for i in stock_ticker: 
    bar_std_height.append(std[i])

bar_roi_height = []

#print(adj_closings.head())
#print(adj_closings[stock_ticker[0]].iloc[0])

for i in range(len(stock_ticker)): 
    current_ticker = stock_ticker[i]
    current_price = adj_closings[stock_ticker[i]].iloc[-1]
    first_price = adj_closings[stock_ticker[i]].iloc[0]
    pricediff = current_price - first_price
    #extrema: max price, min price, max price date, min price date
    extrema[0].append(adj_closings[stock_ticker[i]].max())
    extrema[1].append(adj_closings[stock_ticker[i]].min())
    extrema[2].append(adj_closings.index[adj_closings[stock_ticker[i]] == adj_closings[stock_ticker[i]].max()].tolist())
    extrema[3].append(adj_closings.index[adj_closings[stock_ticker[i]] == adj_closings[stock_ticker[i]].min()].tolist())
    

    current_price_rounded = round(current_price, 2)
    first_price_rounded = round(first_price, 2)
    pricediff_rounded = round(pricediff, 2)

    shares = float(initial_investment) / first_price
    shares_rounded = round(shares, 2)

    profit = shares * pricediff
    profit_rounded = round(profit, 2)

    #roi percentage based off inital investment
    roi = profit / float(initial_investment) * 100
    roi_rounded = round(roi, 2)
    bar_roi_height.append(roi_rounded)

    money_now = float(initial_investment) + profit
    money_now_rounded = round(money_now, 2)






    print('---------------------------------------------------------')
    print("If you bought $" + initial_investment + " of " + current_ticker + " stock on " + start_string + ", you would have been able to buy " + str(shares_rounded) + " shares for an average price of " + str(first_price_rounded) +  ".")
    print("The return from buying " + current_ticker + " on " + start_string + " with an initial investment of $" + initial_investment + " would be $" + str(profit_rounded) + " for a ROI of " + str(roi_rounded) + "%!. You would now have $" + str(money_now_rounded) + ".")
    
print('---------------------------------------------------------')
print("NOTE: these calculations account for stock splits!")

print(extrema)

plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.plot(adj_closings)
plt.ylabel("Price (USD)")
plt.title("Stock Closing Prices")
plt.legend(stock_ticker)
plt.xticks(rotation = 45)

plt.subplot(2, 2, 2)
plt.plot(returns)
plt.ylabel("Return On Investment (USD)")
plt.title("Dollr ROI From $" + str(initial_investment))
plt.legend(stock_ticker)
plt.xticks(rotation = 45)

plt.subplot(2, 2, 3)
plt.bar(range(len(stock_ticker)), bar_std_height)
plt.xticks(range(len(stock_ticker)), stock_ticker)
plt.ylabel('Standard Deviation')
plt.title('Risk Stock Levels')

plt.subplot(2, 2, 4)
plt.bar(range(len(stock_ticker)), bar_roi_height)
plt.xticks(range(len(stock_ticker)), stock_ticker)
plt.ylabel('ROI (%)')
plt.title('RETURN ON INVESTMENT (%)')

plt.subplots_adjust(wspace = .2, hspace = .6)

#fibonacci

plt.figure(figsize=(12, 6))
plt.subplots_adjust(wspace = .2, hspace = .6)
plt.suptitle("Adjusted Closing Prices", fontsize=12, y=0.95)
plt.xticks(rotation = 45)

for i, ticker in enumerate(stock_ticker):
    
    ax = plt.subplot(2, 2, i + 1)
    adj_closings[ticker].plot(ax=ax)
    #ax.hlines(y=extrema[0][i],xmin=extrema[2][i], xmax=dt.datetime.today(),  linewidth=2, alpha = .5,  color='red')
    plt.axhline(y=extrema[0][i], linewidth=2, alpha = .5,  color='red')
    plt.axhline(y=extrema[1][i], linewidth=2, alpha = .5, color='purple')

    difference = extrema[0][i] - extrema[1][i]
    plt.axhline(y=extrema[0][i] - difference * .382,  linewidth=2, alpha = .5, color='orange', linestyle='--')
    plt.axhline(y=extrema[0][i] - difference * .5,  linewidth=2, alpha = .5, color='yellow', linestyle='--')
    plt.axhline(y=extrema[0][i] - difference * .618,  linewidth=2, alpha = .5, color='green', linestyle='--')
    

    ax.set_title(ticker.upper())
    
    



plt.show()







