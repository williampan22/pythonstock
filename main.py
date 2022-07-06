import datetime as dt
from mimetypes import init
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import style 
import pandas as pd
import pandas_datareader
import pandas_datareader.data as web   
from pandas_datareader._utils import RemoteDataError 

valid_ticker = False
valid_investment = False
valid_date = False
num_stocks = 0

while valid_ticker == False: 
    try: 
        str_arr = input('Enter stock tickers: ').split(',') 
        stock_ticker = [num.strip().upper() for num in str_arr]
        
        for i in range(len(stock_ticker)): 
            broken_ticker = stock_ticker[i]
            test = web.DataReader(stock_ticker[i], 'yahoo', dt.datetime(2022, 1, 1), dt.datetime.today())
            
            
        break
    except RemoteDataError: 
        print(broken_ticker + ' was not a valid stock ticker. Try again...' )
    except KeyError: 
        print(broken_ticker + ' was not a valid stock ticker. Try again...' )

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

returns = adj_closings.pct_change()

print(returns)

#print(adj_closings.head())
#print(adj_closings[stock_ticker[0]].iloc[0])

for i in range(len(stock_ticker)): 
    current_ticker = stock_ticker[i]
    current_price = adj_closings[stock_ticker[i]].iloc[-1]
    first_price = adj_closings[stock_ticker[i]].iloc[0]
    pricediff = current_price - first_price

    current_price_rounded = round(current_price, 2)
    first_price_rounded = round(first_price, 2)
    pricediff_rounded = round(pricediff, 2)

    shares = float(initial_investment) / first_price
    shares_rounded = round(shares, 2)

    profit = shares * pricediff
    profit_rounded = round(profit, 2)

    roi = profit / float(initial_investment) * 100
    roi_rounded = round(roi, 2)

    money_now = float(initial_investment) + profit
    money_now_rounded = round(money_now, 2)



    print('---------------------------------------------------------')
    print("If you bought $" + initial_investment + " of " + current_ticker + " stock on " + start_string + ", you would have been able to buy " + str(shares_rounded) + " shares for an average price of " + str(first_price_rounded) +  ".")
    print("The return from buying " + current_ticker + " on " + start_string + " with an initial investment of $" + initial_investment + " would be $" + str(profit_rounded) + " for a ROI of " + str(roi_rounded) + "%!. You would now have $" + str(money_now_rounded) + ".")
    
print('---------------------------------------------------------')
print("NOTE: these calculations account for stock splits!")


adj_closings.plot()
plt.xlabel("Date")
ax = plt.subplot()
plt.ylabel("Adjusted Closing Price")
plt.title("Stock Closing Prices vs Time")
plt.show()

returns.plot()
plt.xlabel("Date")
ax = plt.subplot()
plt.ylabel("returns")
plt.title("returns")
plt.show()





# adj_closings_list = adj_closings.tolist()
# adj_closings_graph = df['Adj Close']
# adj_closings_graph.plot()
# plt.title(stock_ticker + " Closing Price vs Time")
# plt.xlabel('Date')
# plt.ylabel('Adjusted Closing Price')




# plt.show()

# print(df.head())


