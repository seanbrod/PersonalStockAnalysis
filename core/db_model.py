#Sean Broderick
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from connection import Base

class LiveStockData(Base):
    __tablename__ = "live_stock_data"  

    id = Column(String(55), primary_key=True, nullable=False)
    price = Column(Numeric(precision=10, scale=2), primary_key=False, nullable=False)
    time = Column(Integer, primary_key=False, nullable=False)
    date = Column(DateTime, primary_key=True, nullable=False)
    exchange = Column(String(55), primary_key=False, nullable=False)
    quote_type = Column(Integer, primary_key=False, nullable=False)
    market_hours = Column(Integer, primary_key=False, nullable=False)
    percent_change = Column(Numeric(precision=20, scale=10), primary_key=False, nullable=False)
    price_change = Column(Numeric(precision=20, scale=10), primary_key=False, nullable=False)
    price_hint = Column(Integer, primary_key=False, nullable=False)

class LiveFundData(Base):
    __tablename__ = "live_fund_data"  

    id = Column(String(55), primary_key=True, nullable=False)
    price = Column(Numeric(precision=10, scale=2), primary_key=False, nullable=False)
    time = Column(Integer, primary_key=False, nullable=False)
    date = Column(DateTime, primary_key=True, nullable=False)
    exchange = Column(String(55), primary_key=False, nullable=False)
    quote_type = Column(Integer, primary_key=False, nullable=False)
    market_hours = Column(Integer, primary_key=False, nullable=False)
    percent_change = Column(Numeric(precision=20, scale=10), primary_key=False, nullable=False)
    price_change = Column(Numeric(precision=20, scale=10), primary_key=False, nullable=False)
    price_hint = Column(Integer, primary_key=False, nullable=False)


class HistoricalStockData(Base):
    __tablename__ = "historical_stock_data"  

    date = Column(DateTime, primary_key=True, nullable=False)
    open = Column(Numeric(precision=15, scale=5), primary_key=False, nullable=False)
    high = Column(Numeric(precision=15, scale=5), primary_key=False, nullable=False)
    low = Column(Numeric(precision=15, scale=5), primary_key=False, nullable=False)
    close = Column(Numeric(precision=15, scale=5), primary_key=False, nullable=False)
    volume = Column(Integer, primary_key=False, nullable=False)
    dividends = Column(Numeric(precision=10, scale=2), primary_key=False, nullable=False)
    splits = Column(Numeric(precision=10, scale=2), primary_key=False, nullable=False)

class HistoricalFundData(Base):
    __tablename__ = "historical_fund_data"  

    date = Column(DateTime, primary_key=True, nullable=False)
    open = Column(Numeric(precision=15, scale=5), primary_key=False, nullable=False)
    high = Column(Numeric(precision=15, scale=5), primary_key=False, nullable=False)
    low = Column(Numeric(precision=15, scale=5), primary_key=False, nullable=False)
    close = Column(Numeric(precision=15, scale=5), primary_key=False, nullable=False)
    volume = Column(Integer, primary_key=False, nullable=False)
    dividends = Column(Numeric(precision=10, scale=2), primary_key=False, nullable=False)
    splits = Column(Numeric(precision=10, scale=2), primary_key=False, nullable=False)
