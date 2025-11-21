#Sean Broderick
import yfinance as yf
import threading
from typing import Any
from config import stocks, funds, s_set
from pipeline import DBpipeline

db = DBpipeline()

#take in messages of stocks from websocket and add to DB/or send to kafka
def message_handler(message:dict[str, Any]) -> dict[str, Any]:
    #check to see if message is fund or stock then send to respective data injester
    if message["id"] in s_set:
        db.injest_live_sd(message)
    else:
        db.injest_live_fd(message)

# func will create websocket and listen for stocks
def live_stock(st:yf.tickers.Tickers) -> dict[str, Any]:
    st.live(message_handler=message_handler, verbose=True)

# func will create websocket and listen for funds
def live_fund(ft:yf.tickers.Tickers) -> dict[str, Any]:
    ft.live(message_handler=message_handler, verbose=True)

# this func will run two threads for each live ticker websocket
def track_live(st:yf.tickers.Tickers, ft:yf.tickers.Tickers):
    sthread = threading.Thread(target=live_stock, args=(st,))
    fthread = threading.Thread(target=live_fund, args=(ft,))

    sthread.start()
    fthread.start()
    sthread.join()
    fthread.join()

def pull_historic(st:yf.tickers.Tickers, ft:yf.tickers.Tickers):
    #historic data for stock for the day (every minute)   
    print(st.tickers['RTX'].history(period='1d', interval='1m'))

# this func is the main running of the producer
def run():
    db.start()
    # tickers we will track for STOCKS in this project will be Palantir, Meta, Google, RTX (4)
    stock_tickers = yf.Tickers(stocks)
    # tickers we will track for ETFs/Funds in this project will be VOO, SWPPX, SPYD, SCHX, SCHD, SCHA (6)
    fund_tickers = yf.Tickers(funds)


    track_live(stock_tickers, fund_tickers)
    #pull_historic(stock_tickers, fund_tickers)
    db.end()
    
def main():
    run()

if __name__=="__main__":
    main()