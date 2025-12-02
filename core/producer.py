#Sean Broderick
import yfinance as yf
import threading
from typing import Any
from config import stocks, funds, s_set, log
from pipeline import DBpipeline

db = DBpipeline()

#take in messages of stocks from websocket and add to DB/or send to kafka
def message_handler(message:dict[str, Any]) -> dict[str, Any]:
    #check to see if message is fund or stock then send to respective data injester
    log.info(f'message_handler - {message}')
    if message["id"] in s_set:
        db.injest_live_sd(message)
    else:
        db.injest_live_fd(message)

# func will create websocket and listen for stocks
def live_stock(st:yf.tickers.Tickers) -> dict[str, Any]:
    log.info(f'live_stock - Thread Started')
    try:
        st.live(message_handler=message_handler, verbose=True)
    except Exception as e:
        log.exception(f'live_stock - live datas streaming exception: {e}')

# func will create websocket and listen for funds
def live_fund(ft:yf.tickers.Tickers) -> dict[str, Any]:
    log.info(f'live_fund - Thread Started')
    try:
        ft.live(message_handler=message_handler, verbose=True)
    except Exception as e:
        log.exception(f'live_fund - live datas streaming exception: {e}')

# this func will run two threads for each live ticker websocket
def track_live(st:yf.tickers.Tickers, ft:yf.tickers.Tickers):
    sthread = threading.Thread(target=live_stock, args=(st,))
    fthread = threading.Thread(target=live_fund, args=(ft,))

    sthread.start()
    fthread.start()
    sthread.join()
    fthread.join()

# this func is the main running of the producer
def run():
    log.info(f'run - Starting Producer Run')
    db.start()
    
    # tickers we will track for STOCKS in this project will be Palantir, Meta, Google, RTX (4)
    stock_tickers = yf.Tickers(stocks)
    # tickers we will track for ETFs/Funds in this project will be VOO, SWPPX, SPYD, SCHX, SCHD, SCHA (6)
    fund_tickers = yf.Tickers(funds)
    track_live(stock_tickers, fund_tickers)

    db.end()
    log.info(f'run - Ending Producer Run')
    
def main():
    run()

if __name__=="__main__":
    main()