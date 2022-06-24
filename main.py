import datetime as dt
from mimetypes import init
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import style 
import pandas as pd
import pandas_datareader.data as web    

stock_ticker = input('Enter a Stock Ticker: ').upper()
initial_investment = input("Enter an inital investment in dollars: ")
start_string = input('Enter a date in the FORMAT: {Month/Day/Year}: ')

start = dt.datetime.strptime(start_string, "%m/%d/%Y")
end = dt.datetime.today()
timediff = (end-start).days

end_string = end.strftime("%m/%d/%Y")

df = web.DataReader(stock_ticker, 'yahoo', start, end).reset_index()
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

print("If you bought $" + initial_investment + " of " + stock_ticker + " stock on " + start_string + ", you would have been able to buy " + str(shares_rounded) + " shares.")
print(stock_ticker + " closed at $" + str(first_price_rounded) + " on " + start_string + " and closed at $" + str(current_price_rounded) + " today (" + end_string + "). The price difference is " + str(pricediff_rounded))
print("The profit/loss from buying " + stock_ticker + " on " + start_string + " with an initial investment of $" + initial_investment + " would be $" + str(profit_rounded))
print("This is a RETURN ON INVESTMENT (ROI) OF " + str(roi_rounded) + "%! You would now have $" + str(money_now_rounded) + ' compared to the inital investment of $' + initial_investment+ '!')
print("NOTE: these calculations account for stock splits and divident reinvestment!")





