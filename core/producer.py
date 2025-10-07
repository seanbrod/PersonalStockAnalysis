#Sean Broderick
import yfinance as yf
from config import stocks, funds
import threading

#TODO:
# 1. have live data be sent to the pg database (message handler)
# 2. verift that DB works and tables build properly
# 3. set up pipeline.py to have DB operations like adding data. 
# 4. have live producer and then schedule daily historic grab

#take in messages of stocks from websocket and add to DB/or send to kafka
def message_handler(message):
    print("Received message:", message)

# func will create websocket and listen for stocks
def live_stock(st):
    st.live(message_handler=message_handler, verbose=True)

# func will create websocket and listen for funds
def live_fund(ft):
    ft.live(message_handler=message_handler, verbose=True)

# this func will run thwo threads for each live ticker websocket
def track_live(st, ft):
    sthread = threading.Thread(target=None, args=(st,))
    fthread = threading.Thread(target=None, args=(ft,))

    sthread.start()
    fthread.start()
    sthread.join()
    fthread.join()

def pull_historic(st, ft):
    #historic data for stock for the day (every minute)   
    print(st.tickers['RTX'].history(period='1d', interval='1m'))
    
def main():
    # tickers we will track for STOCKS in this project will be Palantir, Meta, Google, RTX (4)
    stock_tickers = yf.Tickers(stocks)

    # tickers we will track for ETFs/Funds in this project will be VOO, SWPPX, SPYD, SCHX, SCHD, SCHA (6)
    fund_tickers = yf.Tickers(funds)

    track_live(stock_tickers, fund_tickers)

if __name__=="__main__":
    main()