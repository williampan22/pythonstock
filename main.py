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

while valid_ticker == False: 
    try: 
        #str_arr = input('Enter stock tickers: ').split(',') 
        #arr = [num.strip().upper() for num in str_arr]
        stock_ticker = input('Enter a Stock Ticker (eg. AAPL): ').upper()
        test = web.DataReader(stock_ticker, 'yahoo', dt.datetime(2022, 1, 1), dt.datetime.today())
        break
    except RemoteDataError: 
        print('That was not a valid stock ticker. Try again...' )
    except KeyError: 
        print('That was not a valid stock ticker. Try again...' )

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


current_price = adj_closings.iloc[-1]
first_price = adj_closings.iloc[0]
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
print("If you bought $" + initial_investment + " of " + stock_ticker + " stock on " + start_string + ", you would have been able to buy " + str(shares_rounded) + " shares.")
print(stock_ticker + " closed at $" + str(first_price_rounded) + " on " + start_string + " and closed at $" + str(current_price_rounded) + " today (" + end_string + "). The price difference is " + str(pricediff_rounded))
print("The profit/loss from buying " + stock_ticker + " on " + start_string + " with an initial investment of $" + initial_investment + " would be $" + str(profit_rounded))
print("This is a RETURN ON INVESTMENT (ROI) OF " + str(roi_rounded) + "%! You would now have $" + str(money_now_rounded) + ' compared to the inital investment of $' + initial_investment+ '!')
print("NOTE: these calculations account for stock splits!")
print('---------------------------------------------------------')


adj_closings_list = adj_closings.tolist()

adj_closings_graph = df['Adj Close']
adj_closings_graph.plot()
plt.title(stock_ticker + " Closing Price vs Time")
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price')




plt.show()

print(df.head())


