#Sean Broderick
from typing import Any 
from datetime import datetime
from connection import Base, SessionLocal, engine
from db_model import *

class DBpipeline():

    def start(self):
        Base.metadata.create_all(engine) #technically only want to do once but overhead not too concerning
        self.session = SessionLocal()
    
    def end(self):
        self.session.close()

    #injest the live STOCK data
    def injest_live_sd(self, msg:dict[str, Any]):

        record = LiveStockData(
            id=msg["id"],
            price=msg["price"],
            time=msg["time"], 
            date=datetime.now(),
            exchange=msg["exchange"],
            quote_type=msg["quote_type"],
            market_hours=msg["market_hours"],
            percent_change=msg["change_percent"],
            price_change=msg["change"],
            price_hint=msg["price_hint"]
        )

        try:
            self.session.add(record)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
    
    #injest the live FUND data
    def injest_live_fd(self, msg:dict[str, Any]):
        record = LiveFundData(
            id=msg["id"],
            price=msg["price"],
            time=msg["time"], 
            date=datetime.now(),
            exchange=msg["exchange"],
            quote_type=msg["quote_type"],
            market_hours=msg["market_hours"],
            percent_change=msg["change_percent"],
            price_change=msg["change"],
            price_hint=msg["price_hint"]
        )

        try:
            self.session.add(record)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e